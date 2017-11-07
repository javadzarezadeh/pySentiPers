from bs4 import BeautifulSoup
import re
from .sentence import Sentence
from .tag import Tag


def get_comment_by_id(path, id):
    """
    Gives all sentences of an specific review.

    Parameters
    ----------
    path: string
        Path of product review XML
    id: string
        ID of desired review
        use 'review' if you want The Review :D

    Returns
    -------
    list of Objects
        Objects are in shape of the Sentence class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')
    sens = []
    if id == 'review':
        review = soup.find('review', id='ReviewBody')
        sentences = review.find_all('sentence')
    else:
        if id.split('-')[0] == 'gr':
            review = soup.find('general_review', id=id)
        elif id.split('-')[0] == 'cr':
            review = soup.find('critical_review', id=id)
        sentences = review.find_all('sentence')
    for sen in sentences:
        sen_id = sen['id']
        sen_text = sen.get_text()
        sen_polarity = sen['value']
        sens.append(Sentence(sen_id, sen_text, sen_polarity))
    return sens


def get_sentence_by_id(path, id):
    """
    Gives the sentences of with the desired ID.

    Parameters
    ----------
    path: string
        Path of product review XML
    id: string
        ID of desired sentence

    Returns
    -------
    Object
        Object is in shape of the Sentence class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')

    sentence = soup.find('sentence', id=id)
    sentence_id = sentence['id']
    sentence_text = sentence.get_text()
    sentence_polarity = sentence['value']
    sentence_obj = Sentence(sentence_id, sentence_text, sentence_polarity)
    return sentence_obj


def get_all_sentences(path, choice):
    """
    Gives all sentences of an specific review XML file.

    Parameters
    ----------
    path: string
        Path of product review XML
    choice: int
        0 used for general reviews
        1 used for critic reviews

    Returns
    -------
    list of Objects
        Objects are in shape of the Sentence class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')

    sens = []
    if choice == 0:
        sentences = soup.find_all('sentence', id=re.compile('^gr'))
    elif choice == 1:
        sentences = soup.find_all('sentence', id=re.compile('^cr'))
    for sen in sentences:
        sen_id = sen['id']
        sen_text = sen.get_text()
        sen_polarity = sen['value']
        sens.append(Sentence(sen_id, sen_text, sen_polarity))
    return sens


def tag_list_by_id(path, id):
    """
    Gives all tags that are related to an specific sentence.

    Parameters
    ----------
    path: string
        Path of product review XML
    id: string
        ID of desired sentence

    Returns
    -------
    list of Objects
        Objects are in shape of the Tag class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')

    tag_list = []
    tags = soup.find_all('tag')
    for tag in tags:
        if tag['type'] != 'Target(M)':
            if tag['coordinate'].split(',')[0].replace('[', '') == id:
                tag_id = tag['id']
                tag_type = tag['type']
                tag_coordinate = tag['coordinate']
                tag_relation = tag['relation']
                tag_polarity = tag['value']
                tag_list.append(Tag(tag_id, tag_type, tag_coordinate, tag_relation, tag_polarity, None))
    return tag_list


def keyword_list_by_id(path, id):
    """
    Gives all keywords that are related to an specific sentence.

    Parameters
    ----------
    path: string
        Path of product review XML
    id: string
        ID of desired sentence

    Returns
    -------
    list of Objects
        Object is in shape of the Sentence class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')

    keyword_list = []
    keywords = soup.find_all('keyword', coordinate=re.compile(id))
    for kw in keywords:
        kw_id = kw['id']
        kw_coordinate = kw['coordinate']
        kw_polarity = kw['value']
        keyword_list.append(Tag(kw_id, None, kw_coordinate, None, kw_polarity, None))
    return keyword_list


def target_list(path):
    """
    Gives all major targets of a review XML file.

    Parameters
    ----------
    path: string
        Path of product review XML

    Returns
    -------
    list of Objects
        Object is in shape of the Sentence class
    """
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')
    targets = []
    tags = soup.find_all('tag', type='Target(M)')
    for tag in tags:
        tag_id = tag['id']
        tag_root = tag['root']
        targets.append(Tag(tag_id, None, None, None, None, tag_root))
    return targets
