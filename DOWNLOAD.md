Dataset **Piling Sheet Image Data** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1OTZfUGlsaW5nIFNoZWV0IEltYWdlIERhdGEvcGlsaW5nLXNoZWV0LWltYWdlLWRhdGEtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiNSt4eDV5aWYzQkh0a2RqUFd0QVhha1V1N1RkaHZ5c0RMcXdwbUNwMG1DND0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Piling Sheet Image Data', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/richiemaskam/piling-sheet-data-2022/download?datasetVersionNumber=1).