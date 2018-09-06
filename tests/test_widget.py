import numpy as np
import pytest
from cornerstone_widget import CornerstoneWidget
from ipywidgets.embed import embed_snippet


def test_ipy():
    c = CornerstoneWidget()
    c.update_image(np.ones((2, 1)))
    widget_state = c.get_state()
    assert widget_state['img_bytes'] == 'AAAAAA=='
    assert widget_state['img_width'] == 2
    assert widget_state['img_height'] == 1
    widget_html = embed_snippet(c)
    assert 'CornerstoneModel' in widget_html, 'Should contain widget code'
    assert 'cornerstone_widget' in widget_html, 'Should contain widget code'


def test_tools():
    c = CornerstoneWidget()
    c.select_tool('pan')
    widget_state = c.get_state()
    assert widget_state['_selected_tool'] == 'pan', 'Should be empty'
    with pytest.raises(NotImplementedError):
        c.select_tool('pane')
