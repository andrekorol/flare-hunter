library(vistime)

df <- read.csv("events.csv")

timeline <- vistime(df, title = "Linha do tempo de eventos detectados na zona ativa (AR) 1158")