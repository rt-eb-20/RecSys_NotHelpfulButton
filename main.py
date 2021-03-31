from processes import read_data

RD = read_data.ReadData()

df_orig = RD.read_file(file_path="data/kindle_reviews.csv.zip",
                     sampling_size=1000)

df = RD.extract_helpful_information(df_orig)
df2 = RD.time_manipulation(df)

print(df2.info())
