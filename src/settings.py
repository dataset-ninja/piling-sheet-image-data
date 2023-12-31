from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Piling Sheet Image Data"
PROJECT_NAME_FULL: str = "Piling Sheet Image Data 2022"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Construction(is_used=False)]
CATEGORY: Category = Category.Construction()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection(), CVTask.Classification()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2022

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/richiemaskam/piling-sheet-data-2022"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2160154
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/piling-sheet-image-data"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/richiemaskam/piling-sheet-data-2022/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://repository.tudelft.nl/islandora/object/uuid:efcf9290-efc4-4b94-8881-c75484873c21"
CITATION_URL: Optional[str] = "https://www.kaggle.com/datasets/richiemaskam/piling-sheet-data-2022"
AUTHORS: Optional[List[str]] = [
    "Richie Maskam",
    "A. (Alireza) Amiri-Simkooei",
    "Sander van Nederveen",
    "Mohammad Fotouhi",
    "Maarten Visser",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["Hrono04@pm.me", "https://www.linkedin.com/in/richie-maskam-40426931/"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Delft University of Technology, Netherlands",
    "Witteveen+Bos, Netherlands",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.tudelft.nl/en/",
    "https://www.witteveenbos.com/nl/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "classification set classes": ["4-grass", "4-metal_good", "4-metal_bad", "4-rock"],
    "classification set classes (alternative)": [
        "6-grass",
        "6-metal_good",
        "6-metal_bad",
        "6-rock",
        "6-metal_acceptable",
        "6-metal_moderate",
    ],
}
TAGS: List[str] = None

SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = ["object detection train"]
##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS
    return settings
