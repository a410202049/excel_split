#!/usr/bin/python
# -*- coding:utf-8  -*-
import xlrd
import xlwt
import os
import math

class Exce:
    # LIMIT = 15 #按多少条分割
    # IS_MULTI = False #是否为多文件，否则就是一个文件多个工作簿
    # IF_TITLE = True #是否有表头
    # HAS_TITLE = True #拆分是否包含表头
    # READ_FILE = None
    SAVE_DIR = None
    FILE_NAME = None
    def __init__(self,limit = 10,read_file = None,is_multi = True,if_title = True,has_title = True):
        """Do nothing, by default."""
        self.LIMIT = limit
        self.IS_MULTI = is_multi
        self.IF_TITLE = if_title
        self.HAS_TITLE = has_title
        self.READ_FILE = read_file

    def open_file(self):
        if not os.path.isfile(self.READ_FILE):
            print u"文件不存在"
            return False
        filepath,file = os.path.split(self.READ_FILE)
        file_name,suffix= os.path.splitext(file)
        self.FILE_NAME = file_name
        self.SUFFIX = suffix
        self.SAVE_DIR = filepath
        if suffix not in ['.xlsx','.xls']:
            print u"文件格式不正确"
            return False
        table_data = xlrd.open_workbook(self.READ_FILE)
        # 获取第一个工作簿
        table = table_data.sheets()[0]
        nrows = table.nrows # 行数
        ncols = table.ncols # 列数
        if self.IF_TITLE:
            nrows = nrows - 1
        number = int(math.ceil(float(nrows) / float(self.LIMIT))) #拆分文件个数
        return table,nrows,ncols,number

    def file_split(self):
        table,row_no,cols_no,number = self.open_file()
        rows_data = table.get_rows()
        data_list = []
        for row in rows_data:
            data = []
            for i in range(0, cols_no):
                value = row[i].value
                value = value if isinstance(value, basestring) else str(value)
                data.append(value)
            data_list.append(data)
        titles = data_list[0] #单独存储表头
        if self.IF_TITLE:
            data_list.pop(0)  #有表头的情况下 删除数据中第一条title数据

        if self.IS_MULTI:
            #多文件
            for i in range(0, number):
                new_file = 'new_'+self.FILE_NAME+'_'+str((i+1))+'.xls'
                workbook = xlwt.Workbook()
                worksheet = workbook.add_sheet('0')

                # 每个文件的数据
                d_list = data_list[i * self.LIMIT:(i + 1) * self.LIMIT]
                # 有表头的情况下
                if self.IF_TITLE:
                    if self.HAS_TITLE:
                        d_list.insert(0, titles) #每个表格插入表头
                for row, row_data in enumerate(d_list):
                    for col, col_data in enumerate(row_data):
                        worksheet.write(row, col, col_data)
                workbook.save(self.SAVE_DIR+os.sep+new_file)
                print self.SAVE_DIR+os.sep+new_file
            print "表格拆分完成"
        else:
            #多工作簿
            new_file = 'new_' + self.FILE_NAME + '.xls'
            workbook = xlwt.Workbook()
            for i in range(0, number):
                sheet_name = 'sheet_' + str((i + 1))
                worksheet = workbook.add_sheet(sheet_name)
                # 每个文件的数据
                d_list = data_list[i * self.LIMIT:(i + 1) * self.LIMIT]
                # 有表头的情况下
                if self.IF_TITLE:
                    if self.HAS_TITLE:
                        d_list.insert(0, titles)  # 每个表格插入表头
                for row, row_data in enumerate(d_list):
                    for col, col_data in enumerate(row_data):
                        worksheet.write(row, col, col_data)
            workbook.save(self.SAVE_DIR+os.sep+new_file)
            print "表格拆分完成"
# e = Exce()
# e.file_split()

