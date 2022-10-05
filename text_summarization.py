from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# from transformers import PegasusModel, PegasusConfig
import torch

#the use of PEGASUS from huggingface to summarize news article

class Pegasus:
    def __init__(self):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # Load tokenizer 
        self.tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        
        # self.configuration = PegasusConfig(num_return_sequences = 5)
        # Load model 
        self.model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        
    def summarize(self, text):
       
        
        tokens = self.tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
        
        # Summarize 
        summary = self.model.generate(**tokens)
        # Decode summary
        result = self.tokenizer.decode(summary[0])
        print(result)
        
        
text = """BERLIN, Sept 26 (Reuters) - Porsche AG shares are poised to price at the top end of the previously announced range, potentially valuing the sports car brand at up to 75 billion euros ($72 billion) in one of Europes biggest ever listings.
Several bookrunners involved in the deal said Porsches books were covered multiple times ahead of the companys market debut on Sept. 29. Volkswagen (VOWG_p.DE), Europe largest carmaker
and Porsche owner, said earlier this month it would price preferred shares at 76.50-82.50 euros, giving a valuation of up to 75 billion euros. 
Orders below the top end of the range risk missing out, as indicated demand has exceeded the full deal size, bookrunners said, with one describing demand as incredibly robust.
Books will close at 1200 GMT on Sept. 28, with shares in Porsche AG, maker of the iconic 911 model, expected to start trading on the Frankfurt stock exchange on Sept. 29.
The strong demand comes despite the fact that valuations of other luxury carmakers, such as Aston Martin and Ferrari, have fallen recently.
At the upper end of the valuation, the listing could be Germany second-largest on record and the biggest in Europe since 1999, Refinitiv data showed.
The bumper flotation, generating between 18.1 billion and 19.5 billion euros, comes at a time when instability in European markets has meant almost no other share sales have taken place.
A total of 911 million Porsche AG shares will be divided into 455.5 million preferred shares and 455.5 million ordinary shares. 
Up to 113,875,000 preferred shares, carrying no voting rights, will be sold to investors over the course of the initial public offering."""

PG = Pegasus()
PG.summarize(text)