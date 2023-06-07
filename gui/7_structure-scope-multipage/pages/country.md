# **Country**{: .color-primary} Statistics

<|layout|columns=1 1 1|gap=30px|
<|{selected_country}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|{selected_representation}|toggle|lov={representation_selector}|on_change=convert_density|>
|>

<br/>

<|layout|columns=1 1 1 1|
<|card m1|
#### **Deaths**{: .color-primary} <br/>
# <|{'{:,}'.format(int(data_country_date.iloc[-1, 6])).replace(',', ' ')}|text|raw|>
|>

<|card m1|
#### **Recovered**{: .color-primary} <br/>
# <|{'{:,}'.format(int(data_country_date.iloc[-1, 5])).replace(',', ' ')}|text|raw|>
|>

<|card m1| 
#### **Confirmed**{: .color-primary} <br/>
# <|{'{:,}'.format(int(data_country_date.iloc[-1, 4])).replace(',', ' ')}|text|raw|>
|>
|>

<br/>

<|layout|columns=2 1|gap=30px|
<|{data_country_date}|chart|type=bar|x=Date|y[3]=Deaths|y[2]=Recovered|y[1]=Confirmed|layout={layout}|options={options}|>

<|{pie_chart}|chart|type=pie|x=values|label=labels|>
|>