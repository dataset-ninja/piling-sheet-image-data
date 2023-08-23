Dataset **Piling Sheet Image Data** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/T/8/IT/p74QHbPwOhHsFu8M2m5dRx42eJcR8cRNKzE5C3fgXTSO7uzpiJUrQjzA1KphMICb6FPUOxPsP94kaxL3S5Oa4i5BohPrrrY0yxIiNp2lxZIbR4ZbaBgZ2gTv7KfL.tar)

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