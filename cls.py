class name:
    def print_name(self,vue):
        return f"my name is {vue}"

class mobile:
    def clean_mobile_numbers(self,df):
        def clean_mobile_number(mobile):
            try:
                mobile_float = float(mobile)
                mobile = "{:.0f}".format(mobile_float)
            except ValueError:
                mobile = str(mobile)

            if mobile.endswith(".0"):
                mobile = mobile[:-2]

            return mobile

        df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
        df['Mobile'] = df['Mobile'].astype(str)
        df = df[df['Mobile'].str.isdigit()]
        df['Mobile'] = df['Mobile'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
        df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
        df['Mobile'] = df['Mobile'].apply(
            lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
        df.drop_duplicates(subset=["Mobile"], inplace=True)
        df.dropna(subset=["Mobile"], inplace=True)

        return df
