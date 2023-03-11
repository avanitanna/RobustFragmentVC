import torchaudio
import random
import torch
class RandomNoiser:
    
    #F.bandpass_biquad(wav,sample_rate=16000,central_freq=800)
    #F.gain(wav,gain_db=5)
    #F.gain(wav,gain_db=0.2)

    def __init__(self):

        self.sample_rate = 16000
        self.device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")

    def pickRandomNoiser(self,wav):

        names = {self.simulateRoomReverberation:"simulateRoomReverberation",self.addBackgroundNoise:"addBackgroundNoise",
                self.applyFilter:"applyFilter",self.applyCodec:"applyCodec",self.simulatePhoneRecording:"simulatePhoneRecording"}

        list_noisers = [self.addBackgroundNoise,self.simulateRoomReverberation,self.simulatePhoneRecording] #self.applyFilter,self.applyCodec,
        noiser_picked = random.choice(list_noisers)
        print("Noiser picked,",names[noiser_picked])
        augmented_wav = noiser_picked(wav)
        pick_loss_or_gain = random.choice([20,-0.1,10,-0.05]) #-1,-2,3,5,10
        augmented_wav = torchaudio.functional.gain(augmented_wav,gain_db=pick_loss_or_gain)
        return augmented_wav

    def simulateRoomReverberation(self,wav): #simulate room reverberation by using Room Impulse Response

        rir_raw, _ = torchaudio.load("SAMPLE_RIR.wav")
        rir_raw = rir_raw.to(self.device)
        rir = rir_raw[:, int(self.sample_rate * 1.01) : int(self.sample_rate * 1.3)]
        rir = rir / torch.norm(rir, p=2)
        RIR = torch.flip(rir, [1])
        wav_ = torch.nn.functional.pad(wav, (RIR.shape[1] - 1, 0)).to(self.device)
        augmented_wav = torch.nn.functional.conv1d(wav_[None, ...], RIR[None, ...])[0]
        return augmented_wav

    def addBackgroundNoise(self,wav): #add background noise/change SNR

        noise, _ = torchaudio.load("SAMPLE_NOISE.wav")
        noise = noise.to(self.device)
        noise = noise[:, : wav.shape[1]]
        
        wav_rms = wav.norm(p=2)
        noise_rms = noise.norm(p=2)

        snr_dbs = [20, 10, 5, 3] #in dB, choose whichever works better
        noisy_wavs = []
        for snr_db in snr_dbs:
            snr = 10 ** (snr_db / 20)
            scale = snr * noise_rms / wav_rms
            noisy_wavs.append((scale * wav + noise) / 2)
        return noisy_wavs[1] #noisy wav 10dB

    def applyFilter(self,wav): #apply lowpass filter and change sample rate
        
        filtered_wav, sample_rate2 = torchaudio.sox_effects.apply_effects_tensor(
            wav,
            self.sample_rate,
            effects=[
                ["lowpass", "4000"],
                [
                    "compand",
                    "0.02,0.05",
                    "-60,-60,-30,-10,-20,-8,-5,-8,-2,-8",
                    "-8",
                    "-7",
                    "0.05",
                ],
                ["rate", "8000"],],)
        return filtered_wav
    
    def applyCodec(self,wav):

        codec_wav = torchaudio.functional.apply_codec(wav, self.sample_rate)
        return codec_wav
    
    def simulatePhoneRecording(self,wav):

        rir_applied = self.simulateRoomReverberation(wav)
        noised_added = self.addBackgroundNoise(rir_applied)
        #filtered = self.applyFilter(noised_added)
        #codec_applied = self.applyCodec(filtered)
        return noised_added




