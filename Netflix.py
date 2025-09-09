import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,15,25]
#
# plt.plot(x,y)
#
# plt.show()
#
#
#
# x = ["monday","tuesday","wednesday","thursday","friday","saturday"]
# y = [10,20,10,15,30,25]
#
# plt.plot(x,y)
#
# plt.title("bakery sales this week")
#
# plt.xlabel("day of the week")
# plt.ylabel("sales per day")
#
# plt.show()



#py.plot(x,y,colour=colour name','linestyle'='line_style','linewidth'=value,'marker'='marker symbol','label'=;label name'

# month = [1,2,3,4]
# sales = [1000,1500,1200,1800]
#
# plt.plot(month,sales,color='black',linestyle='--',linewidth=3,marker='o',label='2025 sales data')
#
# plt.xlabel('month')
# plt.ylabel('sales per month')
# plt.title('monthly sales data report')
# plt.legend(loc='upper left',fontsize=12)
# plt.grid(color='gray',linestyle=':',linewidth=1)
# plt.xlim(1,4)
# plt.ylim(0,2000)
# plt.xticks([1,2,3,4],['m1','m2','m3','m4'])
# plt.savefig("linechart.png")
#
# plt.show()
#
#
#
# #FOR BAR CHART
# #plt.bar(x,y,color='colorname',label='label name')
#
#
#
# product = ['A','B','C','D']
# sales = [1000,1500,900,2000]
#
# plt.bar(product,sales,color='orange',label='sales 2025')
# plt.xlabel('product')
# plt.ylabel('sales per product')
# plt.title('product sales comparison')
# plt.legend()
# plt.savefig("barchart.png",dpi=300,bbox_inches='tight')
#
# plt.show()
#
#
#
# #FOR PIE CHART
# #plt.pie(values,labels='label_list',color='color_name',autopct='%1.1f%%')
#
# region = ["north","south","east","west"]
# revenue = [3000,2000,1500,2500]
#
# plt.pie(revenue,labels=region,autopct='%1.1f%%',colors=['gold','skyblue','purple','green'])
# plt.title("REVENUE CONTRIBUTION BY REGION")
# plt.savefig("piechart.png",dpi=300,bbox_inches='tight')
#
# plt.show()
#
#
#
# #FOR SCATTER PLOT
# #plt.scatter(x,y,colour='colorname',marker='marker_style',label='label_name'
#
# hours_study = [1,2,3,4,5,6,7,8]
# exam_scores = [34,40,45,40,50,60,70,90]
#
# plt.scatter(hours_study,exam_scores,color='green',label='student data')
# plt.xlabel('hours of study')
# plt.ylabel('exam scores')
# plt.title('RELATIONSHIP BETWEEN STUDY TIME AND SCORES')
# plt.legend()
# plt.grid(True)
# plt.savefig('scatterplot.png',dpi=300,bbox_inches='tight')
#
# plt.show()
#
#
# #FOR SUBPLOT
#
#
# x = [1,2,3,4]
# y = [10,20,15,25]
#
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title('line chart')
#
# plt.subplot(1,2,2)
# plt.bar(x,y,color='green')
# plt.title('bar chart')
#
# plt.tight_layout()
# plt.suptitle('COMPARISON BETWEEN LINE AND BAR CHART')
# plt.show()


#NETFLIX DATA ANALYSIS
import pandas as pd

df = pd.read_excel('Netflix dataset.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df)


print(df.info())
print(df.isnull().sum())

df = df.dropna(subset=["director","country"])
print(df)
print(df.isnull().sum())


df["date_added"] = pd.to_datetime(df["date_added"])
print(df)

print(df.info())

print(df.head())
print(df.shape)


type_count = df["type"].value_counts()
plt.bar(type_count.index,type_count.values,color=["red","pink"])
plt.title("NUMBER OF MOVIES VS SHOWS ON NETFLIX")
plt.xlabel("type")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("netflix bar.png",dpi=300,bbox_inches='tight')
plt.show()

#2nd method
# df["type"].value_counts().plot(kind="bar",color=["blue","green"])
# plt.xlabel("type")
# plt.ylabel("count")
# plt.title("movies vs show count")
# plt.tight_layout()
#
# plt.show()


#PIE CHART
rating_counts = df["rating"].value_counts()
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%')
plt.title("PERCENTAGE OF CONTENT RATING")
plt.tight_layout()
plt.savefig("netflix pie.png",dpi=300,bbox_inches='tight')
plt.show()


print()
print(df["type"].value_counts())


country = df["country"].value_counts().head(10)
plt.barh(country.index,country.values,color="red")
plt.title("TOP 10 COUNTRIES WITH MOST CONTENT")
plt.xlabel("number of shows")
plt.ylabel("country")
plt.xticks(rotation=90)
plt.savefig("netflix country.png",dpi=300,bbox_inches='tight')
plt.show()


release_year = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(15,6))
plt.bar(release_year.index,release_year.values,color="red")
plt.title("RELEASE CONTENT PER YEAR")
plt.xlabel("year")
plt.ylabel("count")
plt.xlim(1973,2022)
plt.xticks(release_year.index,rotation=90)
plt.savefig("netflix release.png",dpi=300,bbox_inches='tight')

plt.show()


count_listed = df["listed_in"].value_counts().head(10)
plt.barh(count_listed.index,count_listed.values,color="red")
plt.title("TOP 10 GENRES ON NETFLIX")
plt.xlabel("count")
plt.ylabel("genre")
plt.tight_layout()
plt.savefig("netflix genre.png",dpi=300,bbox_inches='tight')
plt.show()


#FOR SUBPLOT
fig, axs = plt.subplots(3,2,figsize=(20,12))
axs = axs.flatten()

axs[0].bar(type_count.index,type_count.values,color=["red","pink"])
axs[0].set_title("movie vs tv show")

axs[1].pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%')
axs[1].set_title("CONTENT RATING")

axs[2].barh(country.index,country.values,color="red")
axs[2].set_title("TOP 10 COUNTRIES")
axs[2].tick_params(axis='x', labelsize=5)

axs[3].bar(release_year.index,release_year.values,color="red")
axs[3].set_title("RELEASE CONTENT PER YEAR")
axs[3].set_xticks(release_year.index)
axs[3].set_xticklabels(release_year.index,rotation=90,fontsize=5)

axs[4].barh(count_listed.index,count_listed.values,color="red")
axs[4].set_title("TOP 10 GENRES ON NETFLIX")
axs[4].tick_params(axis='x', labelsize=7)

plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.delaxes(axs[5])

plt.suptitle("NETFLIX DATA ANALYSIS",fontsize=20,fontweight='bold')
plt.savefig("netflix data.png",dpi=300,bbox_inches='tight')
plt.show()





