# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# @python_2_unicode_compatible
class Question(models.Model):
    author = models.ForeignKey(User, verbose_name='提问者',)
    question_text = models.TextField('问题陈述')
    number_of_answer = models.IntegerField('回答数', default=0)

    #@python2
    #def __str__(self):
    #   return self.question_text
    def __unicode__(self):
        return self.question_text

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'

# @python_2_unicode_compatible
class Answer(models.Model):
    author = models.ForeignKey(User, verbose_name='回答者')
    question = models.ForeignKey(Question, verbose_name='问题')
    content = models.TextField('回答')

    # def __unicode__(self):
    #   return self.content
    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'
