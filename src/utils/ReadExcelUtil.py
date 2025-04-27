import sys

import pandas as pd
import os
from datetime import datetime

class ReadExcelUtil:
    file_name = "/Users/liu/Code/PycharmProjects/ICEHelper/data/input.xlsx"
    def __init__(self):
        self.df_out_dict = {}
        self.df = None
        print("init readExcelUtil")


    def set_file_name(self, file_name):
        if file_name != "":
            self.file_name = file_name
            return True
        else:
            return False


    def open_file(self, sheet_name):
        if os.path.exists(self.file_name):
            if sheet_name != "":
                self.df = pd.read_excel(self.file_name, sheet_name=sheet_name)

            else:
                self.df = pd.read_excel(self.file_name)

            return self.df
        else:
            return None

    def filter_excel(self, filter_list):
        if len(filter_list) == 0:
            return
        self.df_out_dict.clear()
        for item in filter_list:
            self.df_out_dict.setdefault(item, pd.DataFrame())
        col_name_list = self.df.columns.values
        new_df = self.df.copy()
        for col in col_name_list:
            for item in filter_list:
                if col.startswith(item):
                    if self.df_out_dict.get(item) is not None:
                        self.df_out_dict.get(item)[col] = new_df[col].values
        return self.df_out_dict


    def write_to_excel(self, filter_list, is_split):
        now = datetime.now()
        date_str = now.strftime("%Y%m%d/")
        out_file =os.path.dirname(self.file_name)+"/out/"+date_str

        if not os.path.exists(out_file):
            try:
                os.makedirs(out_file, exist_ok=True)

            except OSError as error:
                return False, error, out_file

        new_df = self.df_out_dict.copy()
        if is_split:
            for item in filter_list:
                if new_df.get(item) is not None:
                    new_df[item].to_excel(out_file + "/"+item+".xlsx", index=False)
        else:
            first_df = self.df_out_dict.get(filter_list[0])
            out = pd.DataFrame()
            for col in range(len(first_df.columns.tolist())):
                for item in filter_list:
                    out[self.df_out_dict.get(item).columns[col]] = self.df_out_dict.get(item).columns[col].values

            out.to_excel("./out/"+date_str +"out_bind.xlsx")
        return True, "输出成功..."

