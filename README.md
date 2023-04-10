# Document classifier tool

## Primary use-case is to help bookkeepers automate their workflows

## Install

- Install docker
<https://www.docker.com/products/docker-desktop/>

- Check that docker is installed

  - Open a Terminal (Mac / Linux) or Powershell (Windows) and check if docker is installed:

    `docker -v`

  - Download the docker image

    `docker run -p 5000:5000 -v $(pwd):/app myflaskapp`

- (Optional) Change the port if 5000 is not available:

    `docker run -p 8080:5000 -v $(pwd):/app myflaskapp`

## Training

Before running the predictor, you'll need to train the tool using existing documents.

- Place your documents on a single location, each type in a separate subfolder, eg:

    on Windows:

        c:\Documents\Invoice
        c:\Documents\Receipts
        c:\Documents\Bank Statements

    on Mac:

        /Users/username/Documents/Invoice
        /Users/username/Documents/Receipts
        /Users/username/Documents/Bank Statements

- On Terminal, navigate to the Documents folder:

`cd /Users/username/Documents`

- Start the tool:

`docker run -p 5000:5000 -v $(pwd):/app myflaskapp`

- Encode your documents folder name in Base64.

  - Navigate to <https://www.base64encode.org/>

  - Copy / Paste your documents folder name, (eg: "Documents").
  
  For the example above:

  unencoded: `Documents`

  encoded: `RG9jdW1lbnRz`

- Open the browser and invoke the "train" endpoint.

    `http://localhost:5000/train/RG9jdW1lbnRz`

This will take some time, say, 20 minutes for 2k documents

Once done, you should see the models created on your current directory. eg:

        /Users/username/classifier.joblib
        /Users/username/vectorizer.joblib

## Running

Now that the model is trained, to predict a document type you'll:

- Encode the relative file path as base 64, eg:

    unencoded: `Documents/MyNewDocument.pdf`

    encoded: `RG9jdW1lbnRzL015TmV3RG9jdW1lbnQucGRm`

- Invoke the Predict endpoint:

    `http://localhost:5000/predict/RG9jdW1lbnRzL015TmV3RG9jdW1lbnQucGRm`

You should see this:

```
{
  "confidence": 0.5432229826918525,
  "type": "Invoice"
}
```
