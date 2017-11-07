import pysentipers as sp

path = '../Sentiment_Datasets/SentiPersV1.0_Extra/SentiPersV1.0/Data/(Canon IXUS 240 HS (PowerShot ELPH 320 HS.xml'

a = sp.get_comment_by_id(path, 'gr-1')
# b = sp.get_sentence_by_id(path, 'cr-1-1')
# c0 = sp.get_all_sentences(path, 0)
# c1 = sp.get_all_sentences(path, 1)
# d = sp.tag_list_by_id(path, 'gr-2-2')
# e = sp.keyword_list_by_id(path, 'gr-1-5')
# f = sp.target_list(path)

print(a[2].text)
