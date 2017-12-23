#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ==============================================================================
#          \file   classification-inference.py
#        \author   chenghuige  
#          \date   2017-11-10 15:32:56.988358
#   \Description  
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys, os

from deepiu.util.classifier import Classifier

import melt

import glob

from collections import namedtuple

import pickle

import tensorflow as tf
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('model_dir', '/home/gezi/mount/temp/image-classification/hotwords/model/inceptionResnetV2.finetune/', '')
flags.DEFINE_string('type', 'valid', '')
flags.DEFINE_string('test_image_dir', '/data2/data/ai_challenger/ai_challenger_caption_validation_20170910/caption_validation_images_20170910/', '')
flags.DEFINE_integer('buffer_size', 300, '')
flags.DEFINE_string('result_file', None, '')
flags.DEFINE_integer('num_image_classes_', 14, '')

m = {}

Result = namedtuple('Result', ['logit', 'prediction'])
def predict(predictor, imgs):
  result = predictor.predict(imgs)
  for img, top_class, top_logit, top_prediction, logit, prediction \
      in zip(imgs, result.top_classes,
             result.top_logits, result.top_predictions,
             result.logits, result.predictions):
    img = os.path.basename(img).replace('.jpg', '')
    if img not in m:
      m[img] = Result(logit, prediction)

def main(_):
  model_dir = FLAGS.model_dir or sys.argv[1]
  assert model_dir
  model_path = melt.get_model_path(model_dir)
  print('model_path:', model_path, file=sys.stderr)

  result_file = './hotword.%s.pkl' % FLAGS.type
  out = open(result_file, 'w')

  predictor = Classifier(model_dir, FLAGS.num_image_classes_)

  imgs = []
  
  print('type', FLAGS.type)
  if FLAGS.type == 'test':
    FLAGS.test_image_dir = '/data2/data/ai_challenger/ai_challenger_caption_test1_20170923/caption_test1_images_20170923/'

  print('test_image_dir', FLAGS.test_image_dir)

  files = glob.glob(FLAGS.test_image_dir + '/*')
  num_files = len(files)
  assert num_files, FLAGS.test_image_dir
  print('num_files to inference', num_files)
  finished = 0
  for img_ in files:
    imgs.append(img_)
    if len(imgs) == FLAGS.buffer_size:
      predict(predictor, imgs)
      finished += len(imgs)
      print('finished:%f' % (finished / float(num_files)), file=sys.stderr, end='\r')
      imgs = []

  if imgs:
    # HACK for nasnet
    while len(imgs) != FLAGS.buffer_size:
      imgs.append(imgs[0])

    predict(predictor, imgs)
    imgs = []

  pickle.dump(m, out)


if __name__ == '__main__':
  tf.app.run()
