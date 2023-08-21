import glob
import os
from collections import defaultdict
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "piling-sheet-data-2022"
    dataset_path = "APP_DATA/archive"
    batch_size = 30
    images_ext = ".jpg"
    bboxes_ext = ".txt"

    ds_name_to_path = {
        "classification": "01-Classification_data/01-Classification_data",
        "object detection train": "02-Object_detection_data/02-Object_detection_data/yolotrain",
        "object detection val": "02-Object_detection_data/02-Object_detection_data/yoloval",
        "test": "03-Model_Test/03-Model_Test",
    }

    def create_ann(image_path):
        labels = []
        tags = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        im_name = get_file_name_with_ext(image_path)

        if ds_name == "classification":
            tags_data = image_name_to_tags[im_name]
            for curr_tag_data in tags_data:
                tag = sly.Tag(curr_tag_data[0])
                tags.append(tag)
            return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)
        else:
            # tag_data = image_name_to_tags[im_name][0]
            # tag = sly.Tag(tag_data)
            # tags.append(tag)
            bbox_name = get_file_name(image_path) + ".txt"
            curr_data_path = image_path[: -len(im_name)]
            bbox_path = os.path.join(curr_data_path, bbox_name)
            if file_exists(bbox_path):
                with open(bbox_path) as f:
                    content = f.read().split("\n")

                    for curr_data in content:
                        if len(curr_data) != 0:
                            curr_data = list(map(float, curr_data.split(" ")))
                            obj_class = idx_to_obj_class[int(curr_data[0])]

                            left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                            right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                            top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                            bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                            rectangle = sly.Rectangle(
                                top=top, left=left, bottom=bottom, right=right
                            )
                            label = sly.Label(rectangle, obj_class)
                            labels.append(label)

            return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    idx_to_obj_class = {
        0: sly.ObjClass("Dim", sly.Rectangle),
        1: sly.ObjClass("Ref", sly.Rectangle),
    }

    obj_classes = list(idx_to_obj_class.values())

    # train_tag = sly.TagMeta("yolotrain", sly.TagValueType.NONE)
    # val_tag = sly.TagMeta("yoloval", sly.TagValueType.NONE)

    tag_names = [
        "4-Grass",
        "4-Metal_Good",
        "4-Metal_Bad",
        "4-Rock",
        "6-Grass",
        "6-Metal_Good",
        "6-Metal_Bad",
        "6-Rock",
        "6-Metal_Acceptable",
        "6-Metal_Moderate",
    ]
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]

    folders = [
        "Data_4_class/Grass",
        "Data_4_class/Metal_Good",
        "Data_4_class/Metal_Bad",
        "Data_4_class/Rock",
        "Data_6_class/Grass",
        "Data_6_class/Metal_Good",
        "Data_6_class/Metal_Bad",
        "Data_6_class/Rock",
        "Data_6_class/Metal_Acceptable",
        "Data_6_class/Metal_Moderate",
    ]

    folder_to_tag_classification = {k: v for k, v in zip(folders, tag_metas)}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes, tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in list(ds_name_to_path.keys()):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        curr_ds_path = os.path.join(dataset_path, ds_name_to_path[ds_name])

        if ds_name != "test":
            image_name_to_tags = defaultdict(list)
            images_pathes = (
                glob.glob(curr_ds_path + "/*/*/*.jpg")
                if ds_name == "classification"
                else glob.glob(curr_ds_path + "/*/*.jpg")
            )
            name_to_path = {}
            for curr_image_path in images_pathes:
                im_name = get_file_name_with_ext(curr_image_path)
                if im_name not in name_to_path:
                    name_to_path[im_name] = curr_image_path
                tag_str = "/".join(curr_image_path.split("/")[-3:-1])
                if ds_name == "classification":
                    tag = folder_to_tag_classification[tag_str]
                    tag_value = folder_to_tag_classification[
                        "/".join(curr_image_path.split("/")[-3:-1])
                    ].name
                    image_name_to_tags[im_name].append((tag, tag_value))
                # elif ds_name == "object detection":
                # tag = folder_to_tag_detection[tag_str]
                # image_name_to_tags[im_name].append((tag))

            images_names = list(name_to_path.keys())

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [name_to_path[image_name] for image_name in img_names_batch]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
                api.annotation.upload_anns(img_ids, anns_batch)

                progress.iters_done_report(len(img_names_batch))

        else:
            images_names = os.listdir(curr_ds_path)
            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))
            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(curr_ds_path, image_name) for image_name in img_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                progress.iters_done_report(len(img_names_batch))
    return project
