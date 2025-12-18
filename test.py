from transformers import pipeline
import torch

def main():
    data = [
        'this movie was horrible, the plot was really boring. acting was okay',
        'the movie is really sucked. there is not plot and acting was bad',
        'what a beautiful movie. great plot. acting was good. will see it again'
    ]

    device = 0 if torch.cuda.is_available() else -1 

    classifier = pipeline(
        'text-classification',
        model='tinybert-sentiment-analysis',
        device=device
    )

    results = classifier(data)
    print(results)

if __name__ == "__main__":
    main()
