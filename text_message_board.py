#!/usr/bin/env python3
# coding: utf-8

"""
文本留言板
python3 text_message_board.py --action=create --text="text" --user=jianxiong
python3 text_message_board.py --action=list --perpage=5 --sort=asc --page=1
python3 text_message_board.py --action=delete --id=1
"""

import sys
import argparse
import os
import json


class TextMessageBoard(object):
    path = "message.txt"

    def __init__(self):
        args = self.args_parse()
        self.action = args['action']
        self.text = args['text']
        self.user = args['user']
        self.perpage = args['perpage']
        self.page = args['page']
        self.sort = args['sort']
        self.id = args['id']
        if self.action == 'create':
            self.message_create()
            pass
        elif self.action == 'list':
            self.message_list()
            pass
        elif self.action == 'delete':
            self.message_delete()
            pass
        else:
            raise ValueError('invalid params action!')

    def args_parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--action', required=True)
        parser.add_argument('--text')
        parser.add_argument('--user')
        parser.add_argument('--perpage', default=5, type=int)
        parser.add_argument('--page', default=1, type=int)
        parser.add_argument('--sort', default='asc')
        parser.add_argument('--id')
        args = parser.parse_args(sys.argv[1:])
        # print("test:", args)
        return vars(args)

    def message_create(self):
        # check
        if self.text is None or self.user is None:
            raise ValueError('missing text or user.')
        if os.path.isfile(self.path):
            with open(self.path, 'r+') as f:
                lines = f.readlines()
                # filter lines
                lines = list(filter(lambda x: x[:-1].strip() != '', lines))
                # empty lines=> write   -1==id=> new-text-id=1      -1=0 => new-text-id=1
                if len(lines) == 0:
                    f.write("id,text,user\n")
                    new_text_id = 1
                else:
                    s = lines[-1].split(',')[0]
                    if s == 'id':
                        new_text_id = 1
                    else:
                        new_text_id = int(s or 0) + 1
        else:
            with open(self.path, 'w') as f:
                f.write("id,text,user\n")
                new_text_id = 1
        # write
        with open(self.path, 'a') as f:
            f.write("%s,%s,%s\n" % (new_text_id, json.dumps(self.text), self.user))
        print('ID:', new_text_id)
        print('Text:', self.text)
        print('User:', self.user)
        print('message created!')

    def message_list(self):
        if self.page <= 0:
            raise ValueError('params page must be greater than 0')
        with open(self.path, 'r') as f:
            lines = f.readlines()
            lines = list(filter(lambda x: x[:-1].strip() != '', lines))
        if len(lines) == 0:
            print('message list is empty.')
            return None
        lines = lines[1:]
        if self.sort == 'desc':
            lines.reverse()
        lines = lines[(self.page - 1) * self.perpage: self.page * self.perpage]
        print('ID Text User')
        for line in lines:
            text = dict(zip(['id', 'text', 'user'], line[:-1].split(',')))
            print(text['id'], json.loads(text['text']), text['user'])

    def message_delete(self):
        if self.id is None:
            raise ValueError('missing params delete id')
        with open(self.path, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                line = line[:-1].strip()
                if line != '' and self.id != str(line.split(',')[0]):
                    f.write(line + "\n")
            f.truncate()
        print('delete id %s success!' % self.id)


if __name__ == '__main__':
    TextMessageBoard()
