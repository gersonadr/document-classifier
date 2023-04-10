import pickle


def save_to_file(filename, model):
    # Save the model to a file
    with open(filename, "wb") as f:
        pickle.dump(model, f)


def load_from_file(filename):
    # Load the model from the fie
    with open(filename, "rb") as f:
        model = pickle.load(f)
        return model
