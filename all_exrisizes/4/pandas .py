# البته، کتابخانه Pandas نیز شامل تعداد زیادی تابع و آپشن است که نمی‌توان همه آن‌ها را در یک پاسخ مطرح کرد. اما به عنوان مثال‌های بیشتر، می‌توانید به موارد زیر مراجعه کنید:

# 1. تابع pd.read_csv(): این تابع برای خواندن فایل های CSV و ساخت دیتافریم از آن‌ها در Pandas استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df)

# 2. تابع pd.DataFrame(): این تابع برای ساخت دیتافریم جدید در Pandas استفاده می‌شود. به عنوان مثال:

import pandas as pd

data = {'Name': ['John', 'Sam', 'Tina'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# 3. تابع df.head(): این تابع برای نمایش چند ردیف اول از دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df.head())

# 4. تابع df.tail(): این تابع برای نمایش چند ردیف آخر از دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df.tail())

# 5. تابع df.describe(): این تابع برای نمایش آماره‌های مختلفی از دیتافریم مانند میانگین، واریانس و کوچکترین و بزرگترین مقدار استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df.describe())

# 6. تابع df.info(): این تابع برای نمایش اطلاعات کلی در مورد دیتافریم مانند تعداد ردیف‌ها، تعداد ستون‌ها و نوع داده‌های هر ستون استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df.info())

# 7. تابع df.drop(): این تابع برای حذف سطر یا ستون از دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
df = df.drop('column_name', axis=1)
print(df)

# 8. تابع df.groupby(): این تابع برای گروه‌بندی داده‌ها بر اساس یک یا چند ستون در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
grouped_data = df.groupby('column_name')
print(grouped_data.mean())

# 9. تابع df.sort_values(): این تابع برای مرتب‌سازی داده‌ها بر اساس یک یا چند ستون در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
sorted_data = df.sort_values('column_name')
print(sorted_data)



# خوشبختانه، Pandas یک کتابخانه بسیار قدرتمند است و دارای تعداد زیادی تابع و آپشن است که می‌توانید از آن‌ها برای کار با داده‌های خود استفاده کنید. به عنوان مثال‌های بیشتر، می‌توانید به موارد زیر مراجعه کنید:

# 10. تابع df.isna(): این تابع برای پیدا کردن مقادیر null یا NaN در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
print(df.isna())

# 11. تابع df.fillna(): این تابع برای جایگذاری مقادیر null یا NaN با مقدار دلخواه در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
df = df.fillna(0)
print(df)

# 12. تابع df.replace(): این تابع برای جایگزینی یک مقدار خاص با مقدار دیگری در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
df = df.replace('old_value', 'new_value')
print(df)

# 13. تابع df.merge(): این تابع برای ادغام دو دیتافریم بر اساس یک یا چند ستون مشترک استفاده می‌شود. به عنوان مثال:

import pandas as pd

df1 = pd.read_csv('example1.csv')
df2 = pd.read_csv('example2.csv')
merged_df = pd.merge(df1, df2, on='column_name')
print(merged_df)

# 14. تابع df.pivot_table(): این تابع برای ساخت جدول محوری از داده‌ها بر اساس یک یا چند ستون در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
pivot_table = df.pivot_table(index='column_name1', columns='column_name2', values='column_name3', aggfunc='mean')
print(pivot_table)

# 15. تابع df.apply(): این تابع برای اعمال یک تابع خاص بر روی هر سطر یا ستون در دیتافریم استفاده می‌شود. به عنوان مثال:

import pandas as pd

df = pd.read_csv('example.csv')
df['column_name'] = df['column_name'].apply(lambda x: x * 2)
print(df)

# این مثال‌ها تنها یک تعداد کمی از توابع و آپشن‌های موجود در Pandas هستند. با استفاده از مستندات رسمی Pandas و جستجو در اینترنت، می‌توانید با توابع بیشتری در این کتابخانه آشنا شوید.