Authors of the Piling Sheet Image Data are asessing the corrosion on piling sheet  and estimating distance between the bumps. Two classificiation algorithm have been made:

1. Classification with ***four*** classes: ***grass***, ***metal good***, ***metal bad*** and ***rock***.
2. Classification with ***six* **classes: ***grass***, ***metal good***, ***metal acceptable***, ***metal moderate*** and ***metal bad*** and ***rock***.

These classes for corrosion were based on [Digigids](https://digigids.hetwaterschapshuis.nl/index.php?album=Bijzondere-constructies-%282019%29/damwand%20of%20beschoeiing/conditie). Grass and rock were included as there was a large amount of it in the raw data-set. See the image below for application of Digigids classes on piling sheet. [![Classes](https://github.com/Harsono-stack/Piling-sheet-assesment-/raw/main/Digiclasses.png)](https://github.com/Harsono-stack/Piling-sheet-assesment-/blob/main/Digiclasses.png) In the ***four*** class data-set, they combined the classes as:

1. Good. Combination of Good and Acceptable.
2. Bad. Combination of Moderate and Bad.

After the assesment the images that have been labeled with ***metal*** will be sent through an Object detection algorithm that was made using YOLOv4. This algorithm was trained to detect: the **bumps** of a piling sheet and a **reference** object. The reference object was something that was seen on most piling sheet in which we know the actual dimension. The horizontal distance between the bumps was calculated and using the reference object we converted the pixel distance into actual distance.

[![Test](https://github.com/Harsono-stack/Piling-sheet-assesment-/raw/main/Yolo_result.png)](https://github.com/Harsono-stack/Piling-sheet-assesment-/blob/main/Yolo_result.png)

The data is part of a raw data-set from Witteveen+Bos N.V. and was remade to be used for image classification and object detection. It consists of high resolution images of a water channel between Lemmer and Delfzijl in The Netherlands. This water channel is going to be wider and deeper so a larger class of ships can pass through. The classification data-sets were made with the help of experts from Witteveen+Bos N.V. and the object detection data-set was made after they made clear which geometric information should be extracted from images.

In general the four class data-set has around 600 images per class and the six class data-set has around 300 images per class. The class ***metal bad***, in the ***six*** class data-set, has around 150 images and more was not available. The object detection data contains the annotation files. The annotation file were created with [LabelImg](https://github.com/heartexlabs/labelImg). There is a seperate model *test* data in which inference was done. The model test set contains 100 images that has all the classes, but are all stored in a folder to simulate unlabeled images in a folder.
