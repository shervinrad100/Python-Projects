from edgar_downloader import write_page
from edgar_downloader import download_files_10k
import pytest
import logging
import os.path
# uncomment if we want to use pytest annotations to skip tests etc:
# import pytest
# pytestmark = pytest.mark.skip("currently skipping part 2 tests - remove or comment this line to test part 2")

# @pytest.mark.skip(reason="I'm assuming this function isn't written") 
def test_write_page():
    result = test_write_page()
    result = os.path.exist(r'\Users\chris\OneDrive\Documents\Kubrick Training\Week 7- Python\Edgar Project\HTMLTest')
    #log_str = "test_2_1_make_list"
    #logging.info('checking:'+ log_str)
    assert result == 'True'
    #logging.info('pass:'+ log_str)



# @pytest.mark.skip(reason="I'm assuming this function isn't written") 
def test_download_files_10k():
    result = est_download_files_10k()


    #log_str = "test_2_1_make_list"
    #logging.info('checking:'+ log_str)
    assert result == ['a', 'b', 'c']
   # logging.info('pass:'+ log_str)