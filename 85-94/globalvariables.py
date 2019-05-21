messageID = 00

myStart = 00

countToMaxLength = 00

durationCounter = 00

message0 = [[04,04,04,00,00,04,00,00,00,04,04,00,00,04,00,04],
            [04,00,00,00,04,00,04,00,04,00,00,00,00,04,00,04],
            [04,00,00,00,04,00,04,00,04,00,00,00,00,04,00,04],
            [04,04,04,00,04,04,04,00,00,04,04,00,00,00,04,00],
            [04,00,00,00,04,00,04,00,00,00,00,04,00,00,04,00],
            [04,00,00,17,04,00,04,00,00,17,00,04,00,00,04,17],
            [04,00,17,17,04,00,04,00,17,17,17,04,00,00,04,17],
            [04,04,04,17,04,17,04,17,04,04,04,17,00,17,04,17]]

message1 = [[04,04,04,00,00,04,00,00,00,04,04,00,00,04,00,04],
            [04,00,00,00,04,00,04,00,04,00,00,00,00,04,00,04],
            [04,00,00,00,04,00,04,00,04,00,00,00,00,04,00,04],
            [04,04,04,17,04,04,04,00,00,04,04,00,00,00,04,17],
            [04,00,17,17,04,00,04,00,17,17,17,04,00,00,04,17],
            [04,17,17,17,04,17,04,17,17,17,17,04,00,17,04,17],
            [04,00,00,17,04,00,04,00,00,17,00,04,00,00,04,17],
            [04,04,04,17,04,00,04,00,04,04,04,00,00,00,04,17]]

message2 = [[04,04,04,00,00,04,00,00,00,04,04,00,00,04,00,04],
            [04,00,00,17,04,00,04,00,04,17,00,00,00,04,00,04],
            [04,00,17,17,04,00,04,00,04,17,17,00,00,04,17,04],
            [04,04,04,17,04,04,04,17,17,04,04,17,00,17,04,17],
            [04,00,00,17,04,00,04,00,00,17,00,04,00,00,04,17],
            [04,00,00,17,04,00,04,00,00,17,00,04,00,00,04,17],
            [04,00,00,17,04,00,04,00,00,17,00,04,17,00,04,17],
            [04,04,04,17,04,17,04,17,04,04,04,17,17,17,04,17]]

message3 = [[04,04,04,17,17,04,00,00,17,04,04,00,00,04,17,04],
            [04,17,17,17,04,17,04,17,04,17,17,17,00,04,17,04],
            [04,00,00,17,04,00,04,00,04,17,00,00,00,04,00,04],
            [04,04,04,17,04,04,04,00,00,04,04,00,00,00,04,17],
            [04,00,00,17,04,00,04,00,00,17,00,04,17,00,04,17],
            [04,17,00,17,04,17,04,17,00,17,00,04,17,17,04,17],
            [04,17,17,00,04,17,04,17,17,00,17,04,17,17,04,00],
            [04,04,04,00,04,00,04,00,04,04,04,00,17,00,04,00]]

message4 = [[04,04,04,17,00,04,00,00,00,04,04,00,00,04,00,04],
            [04,00,00,17,04,00,04,00,04,17,00,00,00,04,00,04],
            [04,00,00,17,04,00,04,00,04,17,00,00,17,04,00,04],
            [04,04,04,17,04,04,04,17,00,04,04,17,17,17,04,17],
            [04,17,17,00,04,17,04,17,17,00,17,04,17,17,04,00],
            [04,00,00,00,04,00,04,00,00,00,00,04,17,00,04,00],
            [04,00,00,00,04,00,04,00,00,00,00,04,17,00,04,00],
            [04,04,04,00,04,00,04,00,04,04,04,00,17,00,04,00]]

message5 = [[03,03,03,00,00,03,03,03,00,00,03,03,00,03,03,03],
            [03,00,00,03,16,03,00,00,00,03,00,00,16,00,03,00],
            [03,16,00,03,00,03,00,00,00,03,00,00,00,16,03,00],
            [03,03,03,00,00,03,03,03,00,00,03,00,00,00,03,00],
            [03,00,00,03,00,03,16,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,16,03,00],
            [03,00,00,03,16,03,00,00,00,00,16,03,16,00,03,00],
            [03,03,03,00,00,03,03,03,00,03,03,16,00,00,03,00]]

message6 = [[03,03,03,00,00,03,03,03,00,00,03,03,00,03,03,03],
            [03,00,00,03,16,03,16,00,00,03,00,00,00,00,03,00],
            [03,16,00,03,00,03,00,00,00,03,00,00,00,16,03,00],
            [03,03,03,00,00,03,03,03,00,00,03,00,16,00,03,00],
            [03,00,00,03,16,03,00,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,16],
            [03,00,16,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,03,03,00,00,03,03,03,00,03,03,16,00,16,03,00]]

message7 = [[03,03,03,00,00,03,03,03,00,00,03,03,00,03,03,03],
            [03,00,00,03,16,03,00,00,00,03,00,00,00,00,03,00],
            [03,16,00,03,00,03,00,00,00,03,00,00,00,00,03,00],
            [03,03,03,00,00,03,03,03,00,00,03,00,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,03,03,00,16,03,03,03,00,03,03,00,00,00,03,00]]

message8 = [[03,03,03,00,00,03,03,03,00,00,03,03,00,03,03,03],
            [03,00,00,03,00,03,00,00,00,03,00,00,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,03,00,00,00,00,03,00],
            [03,03,03,00,00,03,03,03,00,00,03,00,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,00,00,03,00,03,00,00,00,00,00,03,00,00,03,00],
            [03,03,03,00,00,03,03,03,00,03,03,00,00,00,03,00]]
