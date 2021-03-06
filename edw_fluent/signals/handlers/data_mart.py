# -*- coding: utf-8 -*-

import itertools

from django.db.models.signals import (
    pre_delete,
    post_save
)

from edw.models.data_mart import DataMartModel
from edw.signals import make_dispatch_uid
from edw_fluent.models.page import clear_simple_page_buffer


#==============================================================================
# DataMartModel and subclass models event handlers
#==============================================================================
def invalidate_data_mart_after_save(sender, instance, **kwargs):
    """
    Clear simple page buffer
    RUS: Очищает буфер simple_page_buffer после сохранения витрины данных.
    """
    clear_simple_page_buffer()


def invalidate_data_mart_before_delete(sender, instance, **kwargs):
    """
    RUS: Очищает буфер simple_page_buffer перед удалением витрины данных.
    """
    invalidate_data_mart_after_save(sender, instance, **kwargs)

# RUS: Обработчик событий отправляет сигналы после сохранения и перед удалением витрины данных.
Model = DataMartModel.materialized
for clazz in itertools.chain([Model], Model.get_all_subclasses()):
    pre_delete.connect(invalidate_data_mart_before_delete, clazz,
                       dispatch_uid=make_dispatch_uid(pre_delete, invalidate_data_mart_before_delete, clazz))
    post_save.connect(invalidate_data_mart_after_save, clazz,
                      dispatch_uid=make_dispatch_uid(post_save, invalidate_data_mart_after_save, clazz))
