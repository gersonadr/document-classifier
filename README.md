# Document classifier tool

This tool is primarily designed for bookkeepers to automate their workflows, but it can also be utilized by individuals who have an extensive collection of documents and require consistent classification of new documents.

## How it works?

```
curl http:\\localhost:5000\<document_path>

{
  "confidence": 0.5432229826918525,
  "type": "Invoice"
}
```

"Invoice" is one of the possible document types, but it can be tax forms, legal contracts or any document type based on your collection.

The tool currently supports PDFs or image documents. Word/ppt not supported.

## Install

- Install docker
<https://www.docker.com/products/docker-desktop/>

- Check that docker is installed

  - Open a Terminal (Mac / Linux) or Powershell (Windows) and check if docker is installed:

    `docker -v`

  - Download the docker image

    On Mac / Linux:

    `docker run -p 5000:5000 -v $(pwd):/host gersonadr/document-classifier:0.4`

    On Windows:

    `docker run -p 5000:5000 -v ${PWD}:/host gersonadr/document-classifier:0.4`

- (Optional) Change the port if 5000 is not available:

    `docker run -p 8080:5000 -v $(pwd):/host gersonadr/document-classifier:0.4`

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

- On Terminal, navigate to one-up Documents folder:

`cd /Users/username`

- Start the tool:

`docker run -p 5000:5000 -v $(pwd):/host gersonadr/document-classifier:0.4`

- Encode your documents folder name in Base64.

  - Navigate to <https://www.base64encode.org/>

  - Copy / Paste your documents folder name, (eg: "/host/Documents").
  
  For the example above:

  unencoded: `/host/Documents`

  encoded: `L2hvc3QvRG9jdW1lbnRz`

- Open the browser and invoke the "train" endpoint.

    `http://localhost:5000/train/L2hvc3QvRG9jdW1lbnRz`

This will take some time, say, 20 minutes for 2k documents

Once done, you should see the models created on your current directory. eg:

        /Users/username/classifier.joblib
        /Users/username/vectorizer.joblib

## Classify the Document

Now that the model is trained, to predict a new document you'll:

- Encode the relative new document path as base 64, prepended by '/host', eg:

    unencoded: `/host/Documents/MyNewDocument.pdf`

    encoded: `L2hvc3QvRG9jdW1lbnRzL015TmV3RG9jdW1lbnQucGRm`

- Invoke the Predict endpoint:

    `http://localhost:5000/predict/L2hvc3QvRG9jdW1lbnRzL015TmV3RG9jdW1lbnQucGRm`

You should see this:

```
{
  "confidence": 0.5432229826918525,
  "type": "Invoice"
}
```

The confidence level increases with the number of training documents.

Based on experimentation, a confidence level above 80% is considered reliable while anything below 30% is irrelevant.
