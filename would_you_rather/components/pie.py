import  reflex as rx

def pie(data):
    print(data)
    print("AB")
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            label=True,
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300,
    )