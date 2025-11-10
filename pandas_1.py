
import pandas as pd
data_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
data = [1, 2, 3, 4, 5]
#index = ['a', 'b', 'c', 'd', 'e']

s = pd.Series(data, index=data_names, name='Numbers')
s1 = pd.Series(data_names, name='Names')
add= pd.concat([s1,s], axis=1)

#to_csv = add.to_csv('combined_series.csv', index=True)
print(s)

# print(s.max())
# print(s.head(2))
# print(s.tail(2))    

# to_csv = s.to_csv('series_output.csv', index=True)


# print("Series saved to 'series_output.csv'")
