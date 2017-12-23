mkdir -p train.atten.feature.inceptionV4

#python ./imgs2features.py \
#    --image_dir ./caption_train_images_20170902 \
#    --feature_name Mixed_7b \
#    --image_checkpoint_file /home/gezi/data/image_model_check_point/inception_v4.ckpt \
#    | python ./merge-pic-feature.py caption_train_annotations_20170902.txt \
#    > caption_train_annotations_20170902.atten.feature.inceptionV4.txt

#rand.py ./caption_train_annotations_20170902.atten.feature.txt >  ./caption_train_annotations_20170902.atten.feature.rand.txt 
mv ./caption_train_annotations_20170902.atten.feature.inceptionV4.txt \
   ./caption_train_annotations_20170902.atten.feature.inceptionV4.rand.txt

cd ./train.atten.feature.inceptionV4
ln -s ../caption_train_annotations_20170902.atten.feature.inceptionV4.rand.txt .
split.py caption_train_annotations_20170902.atten.feature.inceptionV4.rand.txt 
cd ..


