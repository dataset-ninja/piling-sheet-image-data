import os
from urllib.parse import unquote, urlparse

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s

# def download_dataset(teamfiles_dir: str) -> str:
#     """Use it for large datasets to convert them on the instance"""
#     api = sly.Api.from_env()
#     team_id = sly.env.team_id()
#     storage_dir = sly.app.get_data_dir()

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
#         parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
#         file_name_with_ext = os.path.basename(parsed_url.path)
#         file_name_with_ext = unquote(file_name_with_ext)

#         sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#         local_path = os.path.join(storage_dir, file_name_with_ext)
#         teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)
#         fsize = get_file_size(local_path)
#         with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer..", total=fsize) as pbar:
#             api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
#         dataset_path = unpack_if_archive(local_path)

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
#         for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
#             local_path = os.path.join(storage_dir, file_name_with_ext)
#             teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

#             if not os.path.exists(get_file_name(local_path)):
#                 fsize = get_file_size(local_path)
#                 with tqdm(
#                     desc=f"Downloading '{file_name_with_ext}' to buffer {local_path}...",
#                     total=fsize,
#                     unit="B",
#                     unit_scale=True,
#                 ) as pbar:
#                     api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

#                 sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#                 unpack_if_archive(local_path)
#             else:
#                 sly.logger.info(
#                     f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
#                 )

#         dataset_path = storage_dir
#     return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    pass


#     dataset_path = "/home/iwatkot/supervisely/ninja-datasets/piling-sheet-image-data/02-Object_detection_data/02-Object_detection_data"
#     batch_size = 30
#     images_ext = ".jpg"

#     def create_ann(image_path):
#         labels = []

#         image_np = sly.imaging.image.read(image_path)[:, :, 0]
#         img_height = image_np.shape[0]
#         img_wight = image_np.shape[1]

#         bbox_name = get_file_name(image_path) + ".txt"
#         bbox_path = os.path.join(curr_data_path, bbox_name)
#         if file_exists(bbox_path):
#             with open(bbox_path) as f:
#                 content = f.read().split("\n")

#                 for curr_data in content:
#                     if len(curr_data) != 0:
#                         curr_data = list(map(float, curr_data.split(" ")))
#                         obj_class = idx_to_obj_class[int(curr_data[0])]

#                         left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
#                         right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
#                         top = int((curr_data[2] - curr_data[4] / 2) * img_height)
#                         bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
#                         rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
#                         label = sly.Label(rectangle, obj_class)
#                         labels.append(label)

#         return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

#     idx_to_obj_class = {
#         0: sly.ObjClass("Dim", sly.Rectangle),
#         1: sly.ObjClass("Ref", sly.Rectangle),
#     }

#     obj_classes = list(idx_to_obj_class.values())

#     project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
#     meta = sly.ProjectMeta(obj_classes=obj_classes)
#     api.project.update_meta(project.id, meta.to_json())

#     for curr_folder in os.listdir(dataset_path):
#         ds_name = curr_folder[4:]

#         dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

#         for curr_subfolder in os.listdir(os.path.join(dataset_path, curr_folder)):
#             curr_data_path = os.path.join(dataset_path, curr_folder, curr_subfolder)
#             if dir_exists(curr_data_path):
#                 all_data = os.listdir(curr_data_path)
#                 images_names = [
#                     file_name for file_name in all_data if get_file_ext(file_name) == images_ext
#                 ]

#                 progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

#                 for img_names_batch in sly.batched(images_names, batch_size=batch_size):
#                     images_pathes_batch = [
#                         os.path.join(curr_data_path, image_name) for image_name in img_names_batch
#                     ]

#                     img_infos = api.image.upload_paths(
#                         dataset.id, img_names_batch, images_pathes_batch
#                     )
#                     img_ids = [im_info.id for im_info in img_infos]

#                     anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
#                     api.annotation.upload_anns(img_ids, anns_batch)

#                     progress.iters_done_report(len(img_names_batch))

#     return project
