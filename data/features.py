gate1 = [{
        'name': "WL_FEAT_GATE_1_DESTINATION",
        'readonly': False,
        'addresses': [(8003, 0xFFFF)],
        'minimum': None,
        'maximum': None,
        'description': u"Word per comunicare al PLC che la posizione in cui portare la piastra in uscita",
        'active': True
    },{
        'name': "WL_FEAT_GATE_1_OK_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(8045, 0x0010)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo scan ha avuto successo",
        'active': True
    },{
        'name': "WL_FEAT_GATE_1_KO_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(8045, 0x0020)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo scan non ha avuto successo",
        'active': True
    },{
        'name': "WL_FEAT_GATE_1_REQUEST_SCAN_BARCODE",
        'readonly': True,
        'addresses': [(9000, 0x0080)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC per comunicare la richiesta di scan barcode",
        'active': True
    },{
        'name': "WL_FEAT_GATE_1_GET_SCAN_COMPLETE",
        'readonly': False,
        'addresses': [(8045, 0x0040)],  # D8045.6
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che e' stato preso in carico il termine della fase di lettura del barcode reader",
	'active': True
    },{
        'name': "WL_FEAT_GATE_1_CONNECTED",
        'readonly': False,
        'addresses': [(8045, 0x2000)],  # D8045.13
        'minimum': None,
        'maximum': None,
        'description': u"First gate connected",
        'active': True
    }]

gate2=[
{
        'name': "WL_FEAT_GATE_2_DESTINATION",
        'readonly': False,
        'addresses': [(8005, 0xFFFF)],  # D8005
        'minimum': None,
        'maximum': None,
        'description': u"Word per comunicare al PLC che la posizione in cui portare la piastra in uscita",
        'active': True
    },{
        'name': "WL_FEAT_GATE_2_OK_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(8046, 0x0001)],  # D8046.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo scan ha avuto successo",
        'active': True
    },{
        'name': "WL_FEAT_GATE_2_KO_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(8046, 0x0002)],  # D8046.1
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo scan non ha avuto successo",
        'active': True
    },{
        'name': "WL_FEAT_GATE_2_REQUEST_SCAN_BARCODE",
        'readonly': True,
        'addresses': [(9000, 0x1000)],  # D9000.12
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC per comunicare la richiesta di scan barcode",
        'active': True
    },{
        'name': "WL_FEAT_GATE_2_GET_SCAN_COMPLETE",
        'readonly': False,
        'addresses': [(8046, 0x0004)],  # D8046.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che e' stato preso in carico il termine della fase di lettura del barcode reader",
        'active': True
    },{
        'name': "WL_FEAT_GATE_2_CONNECTED",
        'readonly': False,
        'addresses': [(8046, 0x0010)],  # D8046.4
        'minimum': None,
        'maximum': None,
        'description': u"First gate connected",
        'active': True
    }]
	
globalf=[
{
        'name': "WL_FEAT_GLOBAL_WASP_1_ENABLED",
        'readonly': False,
        'addresses': [(8001, 0x0001)],
        'minimum': None,
        'maximum': None,
        'description': u"Wasp 1 abilitata",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_WASP_2_ENABLED",
        'readonly': False,
        'addresses': [(8001, 0x0002)],
        'minimum': None,
        'maximum': None,
        'description': u"Wasp 2 abilitata",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_1_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0001)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 1 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_2_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0002)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 2 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_3_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0004)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 3 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_4_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0008)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 4 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_5_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0010)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 5 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_6_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0020)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 6 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_7_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0040)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 7 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_8_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0080)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 8 abilitato",
        'active': True
    }, {
        'name': "WL_FEAT_GLOBAL_INC_9_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0100)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 9 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_INC_10_ENABLED",
        'readonly': False,
        'addresses': [(8002, 0x0200)],
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 10 abilitato",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_STOPPEDCYCLE",
        'readonly': True,
        'addresses': [(9000, 0x0004)],  # D9000.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC che comunica al sistema che WaspLab e' in stop ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_STOPCYCLE",
        'readonly': False,
        'addresses': [(8045, 0x0004)],  # D8045.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC lo stop globale del ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_STARTCYCLE",  # D8045.1
        'readonly': False,
        'addresses': [(8045, 0x0002)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC lo start globale del ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_RESETTING",
        'readonly': True,
        'addresses': [(9000, 0x0008)],  # D9000.3
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC che comunica al sistema che WaspLab e' in resetting",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_RESET",
        'readonly': False,
        'addresses': [(8045, 0x0001)],  # D8045.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC il reset globale del ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_PAUSE",
        'readonly': True,
        'addresses': [(9000, 0x0010)],  # D9000.4
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC che comunica al sistema che WaspLab e' in pause",
        'active': True
    },{
        'name': 'WL_FEAT_GLOBAL_INCYCLE',
        'readonly': True,
        'addresses': [(9000, 0x0001)],  # D9000.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC che comunica al sistema che WaspLab e' in ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_STOPPING",
        'readonly': True,
        'addresses': [(9000, 0x0002)],  # D9000.1
        'minimum': None,
        'maximum': None,
        'description': u"Line is stopping",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_READY_TO_START_CYCLE",
        'readonly': True,
        'addresses': [(9000, 0x0100)],  # D9000.8
        'minimum': None,
        'maximum': None,
        'description': u"Bit from the PLC to signal that is ready to start the cycle",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_EMERGENCY",
        'readonly': True,
        'addresses': [(9000, 0x0020)],  # D9000.5
        'minimum': None,
        'maximum': None,
        'description': u"Bit dal PLC che comunica al sistema che WaspLab e' in stop ciclo",
        'active': True
    },{
        'name': "WL_FEAT_GLOBAL_STOP_FOR_UNCORRECT_COMMAND",
        'readonly': False,
        'addresses': [(8045, 0x0008)],  # D8045.3
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che il sw ha problemi. Fermare ciclo",
        'active': True
    },{
        'name': "WL_FEAT_LINE_READY_TO_RESTORE",
        'readonly': True,
        'addresses': [(9000, 0x0400)],  # D9000.10
        'minimum': None,
        'maximum': None,
        'description': u"Bit from the PLC to signal that is ready to restore",
        'active': True
    },{
        'name': "WL_FEAT_LINE_RESET_ALARMS",
        'readonly': False,
        'addresses': [(8045, 0x0400)],  # D8045.10
        'minimum': None,
        'maximum': None,
        'description': u"Reset alarms on the line",
        'active': True
    },{
        'name': "WL_FEAT_LINE_RESET_ALARMS_ACK",
        'readonly': True,
        'addresses': [(9000, 0x0800)],  # D9000.11
        'minimum': None,
        'maximum': None,
        'description': u"Reset alarms on the line ack",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_1",
        'readonly': True,
        'addresses': [(9020, 0xFFFF)],  # D9020
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 1",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_2",
        'readonly': True,
        'addresses': [(9021, 0xFFFF)],  # D9021
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 2",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_3",
        'readonly': True,
        'addresses': [(9022, 0xFFFF)],  # D9022
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 3",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_4",
        'readonly': True,
        'addresses': [(9023, 0xFFFF)],  # D9023
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 4",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_5",
        'readonly': True,
        'addresses': [(9024, 0xFFFF)],  # D9024
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 5",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_6",
        'readonly': True,
        'addresses': [(9025, 0xFFFF)],  # D9025
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 6",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_7",
        'readonly': True,
        'addresses': [(9026, 0xFFFF)],  # D9026
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 7",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_8",
        'readonly': True,
        'addresses': [(9027, 0xFFFF)],  # D9027
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 8",
        'active': True
    }, {
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_9",
        'readonly': True,
        'addresses': [(9028, 0xFFFF)],  # D9028
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 9",
        'active': True
    },{
        'name': "WL_FEAT_LINE_PLATES_IN_UNLOAD_STACKER_10",
        'readonly': True,
        'addresses': [(9029, 0xFFFF)],  # D9029
        'minimum': None,
        'maximum': None,
        'description': u"Number of plates in unload stacker 10",
        'active': True
    },{
        'name': "WL_FEAT_LINE_MUTE_ALARM",
        'readonly': False,
        'addresses': [(8045, 0x1000)],  # D8045.12
        'minimum': None,
        'maximum': None,
        'description': u"Mute acustic alarm on the line",
        'active': True
    },{
        'name': "WL_FEAT_LINE_BUZZER_STATUS",
        'readonly': True,
        'addresses': [(9000, 0x2000)],  # D9000.13
        'minimum': None,
        'maximum': None,
        'description': u"Status of the buzzer",
        'active': True
    },{
        'name': "WL_FEAT_LINE_IN_ALARM",
        'readonly': True,
        'addresses': [(9000, 0x0040)],  # D9000.6
        'minimum': None,
        'maximum': None,
        'description': u"Line is in alarm",
        'active': True
    }]

stackers=[{
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_0_OK",
        'readonly': True,
        'addresses': [(9002, 0x0001)],  # D9002.0
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been put on the load lane (200)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_1_OK",
        'readonly': True,
        'addresses': [(9002, 0x0002)],  # D9002.1
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the first stacker on the load lane (201)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_2_OK",
        'readonly': True,
        'addresses': [(9002, 0x0004)],  # D9002.2
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the second stacker on the load lane (202)",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_0_KO",
        'readonly': True,
        'addresses': [(9009, 0x0001)],  # D9009.0
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been put on the load lane (200)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_1_KO",
        'readonly': True,
        'addresses': [(9009, 0x0002)],  # D9009.1
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the first stacker on the load lane (201)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_LOAD_STACKER_2_KO",
        'readonly': True,
        'addresses': [(9009, 0x0004)],  # D9009.2
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the second stacker on the load lane (202)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_STACKED_ON_LOAD_LANE_OK_ACK",
        'readonly': False,
        'addresses': [(8045, 0x0200)],  # 8045.9
        'minimum': None,
        'maximum': None,
        'description': u"Ack to PLC that media stacked/passed on load lane has been handled (generic for all the stacker on the load lane)",
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_STACKED_ON_LOAD_LANE_KO_ACK",
        'readonly': False,
        'addresses': [(8045, 0x4000)],  # 8045.14
        'minimum': None,
        'maximum': None,
        'description': u"Ack to PLC that media stacked/passed on load lane has been handled (generic for all the stacker on the load lane)",
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_0_OK",
        'readonly': True,
        'addresses': [(9003, 0x0001)],  # D9003.0
        'minimum': None,
        'maximum': None,
        'description': u"A media has just passed on the unload lane final position (100)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_1_OK",
        'readonly': True,
        'addresses': [(9003, 0x0002)],  # D9003.1
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the first stacker on the unload lane (101)",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_2_OK",
        'readonly': True,
        'addresses': [(9003, 0x0004)],  # D9003.2
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the second stacker on the unload lane (102)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_3_OK",
        'readonly': True,
        'addresses': [(9003, 0x0008)],  # D9003.3
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the third stacker on the unload lane (103)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_4_OK",
        'readonly': True,
        'addresses': [(9003, 0x0010)],  # D9003.4
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in the fourth stacker on the unload lane (104)",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_5_OK",
        'readonly': True,
        'addresses': [(9003, 0x0020)],  # D9003.5
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 5 on the unload lane (105)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_6_OK",
        'readonly': True,
        'addresses': [(9003, 0x0040)],  # D9003.6
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 6 on the unload lane (106)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_7_OK",
        'readonly': True,
        'addresses': [(9003, 0x0080)],  # D9003.7
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 7 on the unload lane (107)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_8_OK",
        'readonly': True,
        'addresses': [(9003, 0x0100)],  # D9003.8
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 8 on the unload lane (108)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_9_OK",
        'readonly': True,
        'addresses': [(9003, 0x0200)],  # D9003.9
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 9 on the unload lane (109)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_10_OK",
        'readonly': True,
        'addresses': [(9003, 0x0400)],  # D9003.10
        'minimum': None,
        'maximum': None,
        'description': u"A media has just been pushed in stacker 10 on the unload lane (110)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_0_KO",
        'readonly': True,
        'addresses': [(9008, 0x0001)],  # D9008.0
        'minimum': None,
        'maximum': None,
        'description': u"A media has not passed on the unload lane final position (100)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_1_KO",
        'readonly': True,
        'addresses': [(9008, 0x0002)],  # D9008.1
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in the first stacker on the unload lane (101)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_2_KO",
        'readonly': True,
        'addresses': [(9008, 0x0004)],  # D9008.2
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in the second stacker on the unload lane (102)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_3_KO",
        'readonly': True,
        'addresses': [(9008, 0x0008)],  # D9008.3
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in the third stacker on the unload lane (103)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_4_KO",
        'readonly': True,
        'addresses': [(9008, 0x0010)],  # D9008.4
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in the fourth stacker on the unload lane (104)",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_5_KO",
        'readonly': True,
        'addresses': [(9008, 0x0020)],  # D9008.5
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 5 on the unload lane (105)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_6_KO",
        'readonly': True,
        'addresses': [(9008, 0x0040)],  # D9008.6
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 6 on the unload lane (106)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_7_KO",
        'readonly': True,
        'addresses': [(9008, 0x0080)],  # D9008.7
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 7 on the unload lane (107)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_8_KO",
        'readonly': True,
        'addresses': [(9008, 0x0100)],  # D9008.8
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 8 on the unload lane (108)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_9_KO",
        'readonly': True,
        'addresses': [(9008, 0x0200)],  # D9008.9
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 9 on the unload lane (109)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_10_KO",
        'readonly': True,
        'addresses': [(9008, 0x0400)],  # D9008.10
        'minimum': None,
        'maximum': None,
        'description': u"A media has not been pushed in stacker 10 on the unload lane (110)",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_0_OK_ACK",
        'readonly': False,
        'addresses': [(8046, 0x0008)],  # D8046.3
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the last sensor of the unload lane ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_1_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0002)],  # D8006.1
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_2_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0004)],  # D8006.2
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the second unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_3_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0008)],  # D8006.3
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_4_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0010)],  # D8006.4
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_5_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0020)],  # D8006.5
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 5 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_6_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0040)],  # D8006.6
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 6 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_7_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0080)],  # D8006.7
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 7 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_8_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0100)],  # D8006.8
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 8 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_9_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0200)],  # D8006.9
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 9 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_10_OK_ACK",
        'readonly': False,
        'addresses': [(8006, 0x0400)],  # D8006.10
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 10 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_0_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0001)],  # D8007.1
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the last sensor of the unload lane ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_1_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0002)],  # D8007.1
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_2_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0004)],  # D8007.2
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the second unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_3_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0008)],  # D8007.3
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_4_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0010)],  # D8007.4
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on the first unload stacker ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_5_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0020)],  # D8007.5
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 5 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_6_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0040)],  # D8007.6
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 6 ACK",
        'priority': 10,
        'active': True
    }, {
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_7_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0080)],  # D8007.7
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 7 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_8_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0100)],  # D8007.8
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 8 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_9_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0200)],  # D8007.9
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 9 ACK",
        'priority': 10,
        'active': True
    },{
        'name': "WL_FEAT_MEDIA_ON_UNLOAD_STACKER_10_KO_ACK",
        'readonly': False,
        'addresses': [(8007, 0x0400)],  # D8007.10
        'minimum': None,
        'maximum': None,
        'description': u"Media passed on unload stacker 10 ACK",
        'priority': 10,
        'active': True
    }]

incubator1 =[{
        'name': "WL_FEAT_INC_1_READYTOUNLOAD",
        'readonly': True,
        'addresses': [(14403, 0x0400)],  # D14403.10
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubatore 2 pronto ad accettare i parametri per il ciclo di scarico",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_RESETTING",
        'readonly': True,
        'addresses': [(14403, 0x8000)],  # D14403.15
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubator 2 is resetting",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_DESTINATION",
        'readonly': False,
        'addresses': [(10503, 0xFFFF)],  # D10503
        'minimum': None,
        'maximum': None,
        'description': u"Word che comunica al PLC dove scaricare la piastra dopo uscita da incubatore",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_GET_SCAN_COMPLETE",  # D10545.8
        'readonly': False,
        'addresses': [(10545, 0x0100)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che e' stato preso in carico il termine della fase di lettura del barcode reader",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_START_CYCLE",
        'readonly': False,
        'addresses': [(10545, 0x0080)],  # D10545.7
        'minimum': None,
        'maximum': None,
        'description': u"Request the start of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_RESTORE_CYCLE",
        'readonly': False,
        'addresses': [(10545, 0x0002)],  # D10545.1
        'minimum': None,
        'maximum': None,
        'description': u"Request restore of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STARTUNLOADMEDIA",
        'readonly': False,
        'addresses': [(10545, 0x0004)],  # D10545.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit per richiedere al PLC lo scarico di piastre da incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_OK_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10545, 0x0008)],  # D10545.3
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC OK lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_KO_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10545, 0x0010)],  # D10545.4
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC KO lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PIC_ROUTINE_NEEDED",
        'readonly': False,
        'addresses': [(10545, 0x0200)],  # 10545.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che si necessita un routine di imaging sulla piastra",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PIC_ROUTINE_COMPLETED_SUCCESS",
        'readonly': False,
        'addresses': [(10545, 0x1000)],  # 10545.12
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC la routine di imaging e' stata completata con successo.",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PIC_ROUTINE_STEP_COMPLETED",
        'readonly': False,
        'addresses': [(10545, 0x2000)],  # 10545.13
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo step di imaging attuale e' stato completato (non importa se con successo o no)",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_SUCCESS_LOADED_ACK",
        'readonly': False,
        'addresses': [(10545, 0x4000)],  # D10545.14
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC il sw PC ha ricevuto info riguardo il carico della piastra nell'incubatore.",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_SLOT_TO_CHECK",
        'readonly': False,
        'addresses': [(10501, 0xFFFF)],  # D10501
        'minimum': None,
        'maximum': None,
        'description': u"WORD che indica quale SLOT dell'incubatore 2 scaricare",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MOVE_INCOME_TO_INCUBATOR",
        'readonly': False,
        'addresses': [(10502, 0xFFFF)],  # D10502
        'minimum': None,
        'maximum': None,
        'description': u"Richiede al PLC di spostare la piastra attuale in lettura all'incubatore passato in valore",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PIC_BACKGROUND",
        'readonly': False,
        'addresses': [(10507, 0xFFFF)],  # D10507
        'minimum': None,
        'maximum': None,
        'description': u"Background per imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_START_CONDITIONS_OK",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x0001)],  # D14400.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in condizione di inizio ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_IN_CYCLE",
        'readonly': True,
        'priority': 11,
        'addresses': [(14400, 0x0002)],  # D14400.1
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_REQUEST_SCAN_BARCODE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x0004)],  # D14400.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che la richiesta di scan barcode incubatore 2",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_CONVEYOR_MOVING",
        'readonly': True,
        'priority': 22,
        'addresses': [(14400, 0x0080)],  # D14400.7
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta sta transitando sotto la telecamera dell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CONVEYOR_READY",
        'readonly': True,
        'priority': 21,
        'addresses': [(14400, 0x0100)],  # D14400.8
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta dell incubatore 2 e' pronta per una nuova routine di imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_SUCCESS_LOADED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x0200)],  # D14400.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica la piastra e' stata correttamente caricata nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_UNLOAD_STARTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x0400)],  # D14400.10
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che il e' stato iniziato lo scarico piastra per incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_IN_ALARM",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x2000)],  # D14400.13
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is in an alarm status",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_READY_TO_RESET",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x4000)],  # D14400.14
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is ready to reset",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_EMERGENCY",
        'readonly': True,
        'priority': 10,
        'addresses': [(14400, 0x8000)],  # D14400.15
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 2 in emergenza",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_LOAD_POSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(14401, 0xFFFF)],  # D14401
        'minimum': None,
        'maximum': None,
        'description': u"Posizione di carico della piastra nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_LOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0001)],  # D9005.0
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_LOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0001)],  # D8004.0
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_UNLOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0002)],  # D9005.1
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_UNLOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0002)],  # D8004.1
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(14405, 0x0001)],  # D14405.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_INTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(14405, 0x0004)],  # D14405.2
        'minimum': None,
        'maximum': None,
        'description': u"Media in the first external tongs",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_MEDIA_IN_MANIPULATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14405, 0x0002)],  # D14405.1
        'minimum': None,
        'maximum': None,
        'description': u"Media is in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_EXTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10546, 0x0002)],  # D10546.1
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_INTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10546, 0x0008)],  # D10546.3
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the first external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_MANIPULATOR_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10546, 0x0004)],  # D10546.2
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media being in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MANIPULATOR_POSITION_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10546, 0x0010)],  # D10546.4
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the manipulator position",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CONVEYOR_ON_UNLOADLANE",
        'readonly': True,
        'priority': 30,
        'addresses': [(14404, 0x0100)],  # D14404.8
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is on the load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CONVEYOR_IN_INCUBATOR",
        'readonly': True,
        'priority': 30,
        'addresses': [(14404, 0x0200)],  # D14404.9
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is under the camera in the incubator",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CONVEYOR_POSITION_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0020)],  # D10546.5
        'minimum': None,
        'maximum': None,
        'description': u"ACK for the position of the manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MANIPULATOR_IN_CONVEYOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14404, 0x0400)],  # D14404.10
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''CONVEYOR'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MANIPULATOR_IN_INCUBATOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14404, 0x0800)],  # D14404.11
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''INCUBATOR'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_EXTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14405, 0x0008)],  # D14405.3
        'minimum': None,
        'maximum': None,
        'description': u"The external tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_INTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14405, 0x0010)],  # D14405.4
        'minimum': None,
        'maximum': None,
        'description': u"The internal tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_TONGS_ON_UNLOADLANE_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0100)],  # D10546.8
        'minimum': None,
        'maximum': None,
        'description': u"Tongs on the unloadlane ACK",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_RESET_ALARMS",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0001)],  # D10546.0
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 1",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_RESET_ALARMS_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(14406, 0x0002)],  # D14706.1
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 1 ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_BLOCK_LOADING",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x4000)],  # D10546.14
        'minimum': None,
        'maximum': None,
        'description': u"Block loading of new media",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CONVEYOR_MOVING_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x8000)],  # D10546.15
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the conveyor moving",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STOP_CYCLE",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0080)],  # D10546.7
        'minimum': None,
        'maximum': None,
        'description': u"Request to stop cycle",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MC_CONVEYOR_FORWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10557, 0x0020)],  # D10557.5
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor forward",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MC_CONVEYOR_BACKWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10557, 0x0040)],  # D10557.6
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor backward",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_INCUBATOR_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14405, 0x0020)],  # D14405.5
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_IN_INCUBATOR_MIDDLE_TONGS_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0001)],  # D10547.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MANIPULATOR_IN_MIDDLE_TONGS_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14405, 0x0040)],  # D14405.6
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''MIDDLE_TONGS'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CLEANING_PHOTO_REQUESTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14406, 0x0020)],  # D14406.5
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo'",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_CLEANING_PHOTO_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0004)],  # D10547.2
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo' ack",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_SOFTWARE_ERROR",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0002)],  # D10547.1
        'minimum': None,
        'maximum': None,
        'description': u"Critical error from the software",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_MEDIA_UNLOAD_STARTED_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0008)],  # D10547.3
        'minimum': None,
        'maximum': None,
        'description': u"Incubator unload started ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_LOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14410, 0xFFFF)],  # D14410
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_UNLOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14411, 0xFFFF)],  # D14411
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in unload phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_LOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14412, 0xFFFF)],  # D14412
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_UNLOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14413, 0xFFFF)],  # D14413
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in unload phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_LOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14414, 0xFFFF)],  # D14414
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of loading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_UNLOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14415, 0xFFFF)],  # D14415
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of unloading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14416, 0xFFFF)],  # D14416
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the external togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_INTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14417, 0xFFFF)],  # D14417
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the internal togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STEP_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14418, 0xFFFF)],  # D14418
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the middle togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MUTE_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0800)],  # D10546.11
        'minimum': None,
        'maximum': None,
        'description': u"Mute acustic alarm",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_BARCODE_READER_CONNECTED",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0040)],  # D10547.6
        'minimum': None,
        'maximum': None,
        'description': u"Barcode reader is connected",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_STOPPING",
        'readonly': False,
        'priority': 10,
        'addresses': [(14406, 0x0100)],  # D14406.8
        'minimum': None,
        'maximum': None,
        'description': u"Incubator is stopping",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_MEDIA_ON_LOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14404, 0x0080)],  # D14404.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_LOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10547, 0x0100)],  # D10547.8
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_UNLOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14405, 0x0080)],  # D14405.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_MEDIA_ON_UNLOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10547, 0x0200)],  # D10547.9
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_UPSIDE_DOWN_EXTRACTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10505, 0x0003)],  # D10505/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be extracted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_UPSIDE_DOWN_INSERTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10508, 0x0003)],  # D10508/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be inserted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PLATE_ABSENT_IN_CAROUSEL",
        'readonly': True,
        'priority': 10,
        'addresses': [(14406, 0x0080)],  # D14406.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_PLATE_ABSENT_IN_CAROUSEL_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(10547, 0x0080)],  # D10547.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel ACK",
        'active': True
    }, {
        'name': "WL_FEAT_INC_1_ABSENT_PLATE_SUBPOSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(14407, 0xFFFF)],  # D14407
        'minimum': None,
        'maximum': None,
        'description': u"Subposition of the absent plate requested in the carousel",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_IMAGING_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0010)],  # D10547.4
        'minimum': None,
        'maximum': None,
        'description': u"Generic alarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_IMAGING_PREALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10547, 0x0020)],  # D10547.5
        'minimum': None,
        'maximum': None,
        'description': u"Generic prealarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_BUZZER_STATUS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14406, 0x0040)],  # D14406.6
        'minimum': None,
        'maximum': None,
        'description': u"Status of the buzzer",
        'active': True
    },{
        'name': "WL_FEAT_INC_1_RESET_PLC_PLATES_MEMORY",
        'readonly': False,
        'priority': 10,
        'addresses': [(10546, 0x0200)],  # D10546.9
        'minimum': None,
        'maximum': None,
        'description': u"Reset the plc's memory of all incubated plates",
        'active': True
    }]
	
incubator2 = [
{
        'name': "WL_FEAT_INC_2_READYTOUNLOAD",
        'readonly': True,
        'addresses': [(14703, 0x0400)],  # D14703.10
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubatore 2 pronto ad accettare i parametri per il ciclo di scarico",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_RESETTING",
        'readonly': True,
        'addresses': [(14703, 0x8000)],  # D14703.15
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubator 2 is resetting",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_DESTINATION",
        'readonly': False,
        'addresses': [(10603, 0xFFFF)],  # D10603
        'minimum': None,
        'maximum': None,
        'description': u"Word che comunica al PLC dove scaricare la piastra dopo uscita da incubatore",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_GET_SCAN_COMPLETE",  # D10645.8
        'readonly': False,
        'addresses': [(10645, 0x0100)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che e' stato preso in carico il termine della fase di lettura del barcode reader",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_START_CYCLE",
        'readonly': False,
        'addresses': [(10645, 0x0080)],  # D10645.7
        'minimum': None,
        'maximum': None,
        'description': u"Request the start of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_RESTORE_CYCLE",
        'readonly': False,
        'addresses': [(10645, 0x0002)],  # D10645.1
        'minimum': None,
        'maximum': None,
        'description': u"Request restore of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STARTUNLOADMEDIA",
        'readonly': False,
        'addresses': [(10645, 0x0004)],  # D10645.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit per richiedere al PLC lo scarico di piastre da incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_OK_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10645, 0x0008)],  # D10645.3
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC OK lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_KO_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10645, 0x0010)],  # D10645.4
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC KO lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_PIC_ROUTINE_NEEDED",
        'readonly': False,
        'addresses': [(10645, 0x0200)],  # 10645.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che si necessita un routine di imaging sulla piastra",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_PIC_ROUTINE_COMPLETED_SUCCESS",
        'readonly': False,
        'addresses': [(10645, 0x1000)],  # 10645.12
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC la routine di imaging e' stata completata con successo.",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_PIC_ROUTINE_STEP_COMPLETED",
        'readonly': False,
        'addresses': [(10645, 0x2000)],  # 10645.13
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo step di imaging attuale e' stato completato (non importa se con successo o no)",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_SUCCESS_LOADED_ACK",
        'readonly': False,
        'addresses': [(10645, 0x4000)],  # D10645.14
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC il sw PC ha ricevuto info riguardo il carico della piastra nell'incubatore.",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_SLOT_TO_CHECK",
        'readonly': False,
        'addresses': [(10601, 0xFFFF)],  # D10601
        'minimum': None,
        'maximum': None,
        'description': u"WORD che indica quale SLOT dell'incubatore 2 scaricare",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MOVE_INCOME_TO_INCUBATOR",
        'readonly': False,
        'addresses': [(10602, 0xFFFF)],  # D10602
        'minimum': None,
        'maximum': None,
        'description': u"Richiede al PLC di spostare la piastra attuale in lettura all'incubatore passato in valore",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_PIC_BACKGROUND",
        'readonly': False,
        'addresses': [(10607, 0xFFFF)],  # D10607
        'minimum': None,
        'maximum': None,
        'description': u"Background per imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_START_CONDITIONS_OK",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x0001)],  # D14700.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in condizione di inizio ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_IN_CYCLE",
        'readonly': True,
        'priority': 11,
        'addresses': [(14700, 0x0002)],  # D14700.1
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_REQUEST_SCAN_BARCODE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x0004)],  # D14700.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che la richiesta di scan barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CONVEYOR_MOVING",
        'readonly': True,
        'priority': 22,
        'addresses': [(14700, 0x0080)],  # D14700.7
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta sta transitando sotto la telecamera dell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CONVEYOR_READY",
        'readonly': True,
        'priority': 21,
        'addresses': [(14700, 0x0100)],  # D14700.8
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta dell incubatore 2 e' pronta per una nuova routine di imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_SUCCESS_LOADED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x0200)],  # D14700.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica la piastra e' stata correttamente caricata nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_UNLOAD_STARTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x0400)],  # D14700.10
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che il e' stato iniziato lo scarico piastra per incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_IN_ALARM",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x2000)],  # D14700.13
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is in an alarm status",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_READY_TO_RESET",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x4000)],  # D14700.14
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is ready to reset",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_EMERGENCY",
        'readonly': True,
        'priority': 10,
        'addresses': [(14700, 0x8000)],  # D14700.15
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 2 in emergenza",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_LOAD_POSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(14701, 0xFFFF)],  # D14701
        'minimum': None,
        'maximum': None,
        'description': u"Posizione di carico della piastra nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_LOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0004)],  # D9005.2
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane - DEPRECATED",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_MEDIA_ON_LOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0004)],  # D8004.2
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_UNLOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0008)],  # D9005.3
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane - DEPRECATED",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_MEDIA_ON_UNLOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0008)],  # D8004.3
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(14705, 0x0001)],  # D14705.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_INTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(14705, 0x0004)],  # D14705.2
        'minimum': None,
        'maximum': None,
        'description': u"Media in the first external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_MANIPULATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14705, 0x0002)],  # D14705.1
        'minimum': None,
        'maximum': None,
        'description': u"Media is in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_EXTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10646, 0x0002)],  # D10646.1
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_INTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10646, 0x0008)],  # D10646.3
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the first external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_MANIPULATOR_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10646, 0x0004)],  # D10646.2
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media being in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MANIPULATOR_POSITION_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10646, 0x0010)],  # D10646.4
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the manipulator position",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_CONVEYOR_ON_UNLOADLANE",
        'readonly': True,
        'priority': 30,
        'addresses': [(14704, 0x0100)],  # D14704.8
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is on the load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CONVEYOR_IN_INCUBATOR",
        'readonly': True,
        'priority': 30,
        'addresses': [(14704, 0x0200)],  # D14704.9
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is under the camera in the incubator",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CONVEYOR_POSITION_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0020)],  # D10646.5
        'minimum': None,
        'maximum': None,
        'description': u"ACK for the position of the manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MANIPULATOR_IN_CONVEYOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14704, 0x0400)],  # D14704.10
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''CONVEYOR'' position",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_MANIPULATOR_IN_INCUBATOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14704, 0x0800)],  # D14704.11
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''INCUBATOR'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_EXTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14705, 0x0008)],  # D14705.3
        'minimum': None,
        'maximum': None,
        'description': u"The external tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_INTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14705, 0x0010)],  # D14705.4
        'minimum': None,
        'maximum': None,
        'description': u"The internal tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_TONGS_ON_UNLOADLANE_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0100)],  # D10646.8
        'minimum': None,
        'maximum': None,
        'description': u"Tongs on the unloadlane ACK",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_RESET_ALARMS",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0001)],  # D10646.0
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_RESET_ALARMS_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(14706, 0x0002)],  # D14706.1
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 2 ack",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_BLOCK_LOADING",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x4000)],  # D10646.14
        'minimum': None,
        'maximum': None,
        'description': u"Block loading of new media",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CONVEYOR_MOVING_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x8000)],  # D10646.15
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the conveyor moving",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STOP_CYCLE",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0080)],  # D10646.7
        'minimum': None,
        'maximum': None,
        'description': u"Request to stop cycle",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MC_CONVEYOR_FORWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10657, 0x0020)],  # D10657.5
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor forward",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_MC_CONVEYOR_BACKWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10657, 0x0040)],  # D10657.6
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor backward",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_INCUBATOR_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14705, 0x0020)],  # D14705.5
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_IN_INCUBATOR_MIDDLE_TONGS_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0001)],  # D10647.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MANIPULATOR_IN_MIDDLE_TONGS_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(14705, 0x0040)],  # D14705.6
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''MIDDLE_TONGS'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_CLEANING_PHOTO_REQUESTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(14706, 0x0020)],  # D14706.5
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo'",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_CLEANING_PHOTO_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0004)],  # D10647.2
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo' ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_SOFTWARE_ERROR",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0002)],  # D10647.1
        'minimum': None,
        'maximum': None,
        'description': u"Critical error from the software",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_UNLOAD_STARTED_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0008)],  # D10647.3
        'minimum': None,
        'maximum': None,
        'description': u"Incubator unload started ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_LOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14710, 0xFFFF)],  # D14710
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_UNLOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14711, 0xFFFF)],  # D14711
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in unload phase",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_STEP_LOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14712, 0xFFFF)],  # D14712
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_UNLOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(14713, 0xFFFF)],  # D14713
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in unload phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_LOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14714, 0xFFFF)],  # D14714
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of loading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_UNLOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(14715, 0xFFFF)],  # D14715
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of unloading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14716, 0xFFFF)],  # D14716
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the external togs",
        'active': True
    }, {
        'name': "WL_FEAT_INC_2_STEP_INTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14717, 0xFFFF)],  # D14717
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the internal togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STEP_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14718, 0xFFFF)],  # D14718
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the middle togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MUTE_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0800)],  # D10646.11
        'minimum': None,
        'maximum': None,
        'description': u"Mute acustic alarm",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_BARCODE_READER_CONNECTED",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0040)],  # D10647.6
        'minimum': None,
        'maximum': None,
        'description': u"Barcode reader is connected",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_STOPPING",
        'readonly': False,
        'priority': 10,
        'addresses': [(14706, 0x0100)],  # D14706.8
        'minimum': None,
        'maximum': None,
        'description': u"Incubator is stopping",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_LOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14704, 0x0080)],  # D14704.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_LOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10647, 0x0100)],  # D10647.8
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_UNLOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(14705, 0x0080)],  # D14705.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_MEDIA_ON_UNLOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10647, 0x0200)],  # D10647.9
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_UPSIDE_DOWN_EXTRACTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10605, 0x0003)],  # D10605/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be extracted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_UPSIDE_DOWN_INSERTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10608, 0x0003)],  # D10608/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be inserted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_PLATE_ABSENT_IN_CAROUSEL",
        'readonly': True,
        'priority': 10,
        'addresses': [(14706, 0x0080)],  # D14706.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_PLATE_ABSENT_IN_CAROUSEL_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(10647, 0x0080)],  # D10647.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel ACK",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_ABSENT_PLATE_SUBPOSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(14707, 0xFFFF)],  # D14707
        'minimum': None,
        'maximum': None,
        'description': u"Subposition of the absent plate requested in the carousel",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_IMAGING_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10567, 0x0010)],  # D10647.4
        'minimum': None,
        'maximum': None,
        'description': u"Generic alarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_IMAGING_PREALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10647, 0x0020)],  # D10647.5
        'minimum': None,
        'maximum': None,
        'description': u"Generic pre alarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_BUZZER_STATUS",
        'readonly': True,
        'priority': 10,
        'addresses': [(14706, 0x0040)],  # D14706.6
        'minimum': None,
        'maximum': None,
        'description': u"Status of the buzzer",
        'active': True
    },{
        'name': "WL_FEAT_INC_2_RESET_PLC_PLATES_MEMORY",
        'readonly': False,
        'priority': 10,
        'addresses': [(10646, 0x0200)],  # D10646.9
        'minimum': None,
        'maximum': None,
        'description': u"Reset the plc's memory of all incubated plates",
        'active': True
    }]

incubator3 = [
	{
        'name': "WL_FEAT_INC_3_READYTOUNLOAD",
        'readonly': True,
        'addresses': [(15003, 0x0400)],  # D15003.10
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubatore 2 pronto ad accettare i parametri per il ciclo di scarico",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_RESETTING",
        'readonly': True,
        'addresses': [(15003, 0x8000)],  # D15003.15
        'minimum': None,
        'maximum': None,
        'priority': 10,
        'description': u"Incubator 2 is resetting",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_DESTINATION",
        'readonly': False,
        'addresses': [(10703, 0xFFFF)],  # D10703
        'minimum': None,
        'maximum': None,
        'description': u"Word che comunica al PLC dove scaricare la piastra dopo uscita da incubatore",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_GET_SCAN_COMPLETE",  # D10745.8
        'readonly': False,
        'addresses': [(10745, 0x0100)],
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che e' stato preso in carico il termine della fase di lettura del barcode reader",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_START_CYCLE",
        'readonly': False,
        'addresses': [(10745, 0x0080)],  # D10745.7
        'minimum': None,
        'maximum': None,
        'description': u"Request the start of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_RESTORE_CYCLE",
        'readonly': False,
        'addresses': [(10745, 0x0002)],  # D10745.1
        'minimum': None,
        'maximum': None,
        'description': u"Request restore of the cycle from the operator's PC",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STARTUNLOADMEDIA",
        'readonly': False,
        'addresses': [(10745, 0x0004)],  # D10745.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit per richiedere al PLC lo scarico di piastre da incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_OK_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10745, 0x0008)],  # D10745.3
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC OK lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_KO_SCAN_BARCODE",
        'readonly': False,
        'addresses': [(10745, 0x0010)],  # D10745.4
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC KO lettura barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_PIC_ROUTINE_NEEDED",
        'readonly': False,
        'addresses': [(10745, 0x0200)],  # 10745.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che si necessita un routine di imaging sulla piastra",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_PIC_ROUTINE_COMPLETED_SUCCESS",
        'readonly': False,
        'addresses': [(10745, 0x1000)],  # 10745.12
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC la routine di imaging e' stata completata con successo.",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_PIC_ROUTINE_STEP_COMPLETED",
        'readonly': False,
        'addresses': [(10745, 0x2000)],  # 10745.13
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC che lo step di imaging attuale e' stato completato (non importa se con successo o no)",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_SUCCESS_LOADED_ACK",
        'readonly': False,
        'addresses': [(10745, 0x4000)],  # D10745.14
        'minimum': None,
        'maximum': None,
        'description': u"Bit per comunicare al PLC il sw PC ha ricevuto info riguardo il carico della piastra nell'incubatore.",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_SLOT_TO_CHECK",
        'readonly': False,
        'addresses': [(10701, 0xFFFF)],  # D10701
        'minimum': None,
        'maximum': None,
        'description': u"WORD che indica quale SLOT dell'incubatore 2 scaricare",
        'active': True
    }, {
        'name': "WL_FEAT_INC_3_MOVE_INCOME_TO_INCUBATOR",
        'readonly': False,
        'addresses': [(10702, 0xFFFF)],  # D10702
        'minimum': None,
        'maximum': None,
        'description': u"Richiede al PLC di spostare la piastra attuale in lettura all'incubatore passato in valore",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_PIC_BACKGROUND",
        'readonly': False,
        'addresses': [(10707, 0xFFFF)],  # D10707
        'minimum': None,
        'maximum': None,
        'description': u"Background per imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_START_CONDITIONS_OK",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x0001)],  # D15000.0
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in condizione di inizio ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_IN_CYCLE",
        'readonly': True,
        'priority': 11,
        'addresses': [(15000, 0x0002)],  # D15000.1
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica incubatore 2 in ciclo",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_REQUEST_SCAN_BARCODE",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x0004)],  # D15000.2
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che la richiesta di scan barcode incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_MOVING",
        'readonly': True,
        'priority': 22,
        'addresses': [(15000, 0x0080)],  # D15000.7
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta sta transitando sotto la telecamera dell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_READY",
        'readonly': True,
        'priority': 21,
        'addresses': [(15000, 0x0100)],  # D15000.8
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che la slitta dell incubatore 2 e' pronta per una nuova routine di imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_SUCCESS_LOADED",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x0200)],  # D15000.9
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica la piastra e' stata correttamente caricata nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_UNLOAD_STARTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x0400)],  # D15000.10
        'minimum': None,
        'maximum': None,
        'description': u"Bit girato dal PLC che indica che il e' stato iniziato lo scarico piastra per incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_IN_ALARM",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x2000)],  # D15000.13
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is in an alarm status",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_READY_TO_RESET",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x4000)],  # D15000.14
        'minimum': None,
        'maximum': None,
        'description': u"The incubator is ready to reset",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_EMERGENCY",
        'readonly': True,
        'priority': 10,
        'addresses': [(15000, 0x8000)],  # D15000.15
        'minimum': None,
        'maximum': None,
        'description': u"Incubatore 2 in emergenza",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_LOAD_POSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(15001, 0xFFFF)],  # D15001
        'minimum': None,
        'maximum': None,
        'description': u"Posizione di carico della piastra nell incubatore 2",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_LOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0010)],  # D9005.4
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_LOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0010)],  # D8004.4
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_UNLOAD_LANE_OLD",
        'readonly': True,
        'priority': 10,
        'addresses': [(9005, 0x0020)],  # D9005.5
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_UNLOAD_LANE_ACK_OLD",
        'readonly': False,
        'priority': 1,
        'addresses': [(8004, 0x0020)],  # D8004.5
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane - DEPRECATED",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(15005, 0x0001)],  # D15005.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_INTERNAL_TONGS",
        'readonly': True,
        'priority': 20,
        'addresses': [(15005, 0x0004)],  # D15005.2
        'minimum': None,
        'maximum': None,
        'description': u"Media in the first external tongs",
        'active': True
    }, {
        'name': "WL_FEAT_INC_3_MEDIA_IN_MANIPULATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(15005, 0x0002)],  # D15005.1
        'minimum': None,
        'maximum': None,
        'description': u"Media is in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_EXTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10746, 0x0002)],  # D10746.1
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the second external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_INTERNAL_TONGS_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10746, 0x0008)],  # D10746.3
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media in the first external tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_MANIPULATOR_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10746, 0x0004)],  # D10746.2
        'minimum': None,
        'maximum': None,
        'description': u"ACK of Media being in manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MANIPULATOR_POSITION_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10746, 0x0010)],  # D10746.4
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the manipulator position",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_ON_UNLOADLANE",
        'readonly': True,
        'priority': 30,
        'addresses': [(15004, 0x0100)],  # D15004.8
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is on the load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_IN_INCUBATOR",
        'readonly': True,
        'priority': 30,
        'addresses': [(15004, 0x0200)],  # D15004.9
        'minimum': None,
        'maximum': None,
        'description': u"The conveyor is under the camera in the incubator",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_POSITION_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0020)],  # D10746.5
        'minimum': None,
        'maximum': None,
        'description': u"ACK for the position of the manipulator",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MANIPULATOR_IN_CONVEYOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(15004, 0x0400)],  # D15004.10
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''CONVEYOR'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MANIPULATOR_IN_INCUBATOR_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(15004, 0x0800)],  # D15004.11
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''INCUBATOR'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_EXTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(15005, 0x0008)],  # D15005.3
        'minimum': None,
        'maximum': None,
        'description': u"The external tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_INTERNAL_TONGS_ON_UNLOADLANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(15005, 0x0010)],  # D15005.4
        'minimum': None,
        'maximum': None,
        'description': u"The internal tongs is on the unloadlane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_TONGS_ON_UNLOADLANE_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0100)],  # D10746.8
        'minimum': None,
        'maximum': None,
        'description': u"Tongs on the unloadlane ACK",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_RESET_ALARMS",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0001)],  # D10746.0
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 1",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_RESET_ALARMS_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(15006, 0x0002)],  # D14706.1
        'minimum': None,
        'maximum': None,
        'description': u"Reset Alarms on incubator 1 ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_BLOCK_LOADING",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x4000)],  # D10746.14
        'minimum': None,
        'maximum': None,
        'description': u"Block loading of new media",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CONVEYOR_MOVING_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x8000)],  # D10746.15
        'minimum': None,
        'maximum': None,
        'description': u"Ack of the conveyor moving",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STOP_CYCLE",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0080)],  # D10746.7
        'minimum': None,
        'maximum': None,
        'description': u"Request to stop cycle",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MC_CONVEYOR_FORWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10757, 0x0020)],  # D10757.5
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor forward",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MC_CONVEYOR_BACKWARD",
        'readonly': False,
        'priority': 10,
        'addresses': [(10757, 0x0040)],  # D10757.6
        'minimum': None,
        'maximum': None,
        'description': u"Manual command conveyor backward",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_INCUBATOR_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(15005, 0x0020)],  # D15005.5
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_IN_INCUBATOR_MIDDLE_TONGS_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0001)],  # D10747.0
        'minimum': None,
        'maximum': None,
        'description': u"Media in the incubator middle tongs ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MANIPULATOR_IN_MIDDLE_TONGS_POSITION",
        'readonly': True,
        'priority': 30,
        'addresses': [(15005, 0x0040)],  # D15005.6
        'minimum': None,
        'maximum': None,
        'description': u"The manipulator is in ''MIDDLE_TONGS'' position",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CLEANING_PHOTO_REQUESTED",
        'readonly': True,
        'priority': 10,
        'addresses': [(15006, 0x0020)],  # D15006.5
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo'",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_CLEANING_PHOTO_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0004)],  # D10747.2
        'minimum': None,
        'maximum': None,
        'description': u"The PLC is ready to do the 'cleaning photo' ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_SOFTWARE_ERROR",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0002)],  # D10747.1
        'minimum': None,
        'maximum': None,
        'description': u"Critical error from the software",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_UNLOAD_STARTED_ACK",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0008)],  # D10747.3
        'minimum': None,
        'maximum': None,
        'description': u"Incubator unload started ack",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_LOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(15010, 0xFFFF)],  # D15010
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_UNLOAD_READING",
        'readonly': True,
        'priority': 10,
        'addresses': [(15011, 0xFFFF)],  # D15011
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of reading in unload phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_LOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(15012, 0xFFFF)],  # D15012
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in load phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_UNLOAD_IMAGING",
        'readonly': True,
        'priority': 10,
        'addresses': [(15013, 0xFFFF)],  # D15013
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of imaging in unload phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_LOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(15014, 0xFFFF)],  # D15014
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of loading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_UNLOAD_INCUBATOR",
        'readonly': True,
        'priority': 10,
        'addresses': [(15015, 0xFFFF)],  # D15015
        'minimum': None,
        'maximum': None,
        # AAAAAAAAAAAAA le descrizioni di guido...
        'description': u"PLC's step of unloading in 'incubator' phase",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_EXTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(15016, 0xFFFF)],  # D15016
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the external togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_INTERNAL_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(15017, 0xFFFF)],  # D15017
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the internal togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STEP_MIDDLE_TONGS",
        'readonly': True,
        'priority': 10,
        'addresses': [(15018, 0xFFFF)],  # D15018
        'minimum': None,
        'maximum': None,
        'description': u"PLC's step of the middle togs",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MUTE_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0800)],  # D10746.11
        'minimum': None,
        'maximum': None,
        'description': u"Mute acustic alarm",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_BARCODE_READER_CONNECTED",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0040)],  # D10747.6
        'minimum': None,
        'maximum': None,
        'description': u"Barcode reader is connected",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_STOPPING",
        'readonly': False,
        'priority': 10,
        'addresses': [(15006, 0x0100)],  # D15006.8
        'minimum': None,
        'maximum': None,
        'description': u"Incubator is stopping",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_LOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(15004, 0x0080)],  # D15004.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on load lane",
        'active': True
    }, {
        'name': "WL_FEAT_INC_3_MEDIA_ON_LOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10747, 0x0100)],  # D10747.8
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on load lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_UNLOAD_LANE",
        'readonly': True,
        'priority': 10,
        'addresses': [(15005, 0x0080)],  # D15005.7
        'minimum': None,
        'maximum': None,
        'description': u"Media has been put on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_MEDIA_ON_UNLOAD_LANE_ACK",
        'readonly': False,
        'priority': 1,
        'addresses': [(10747, 0x0200)],  # D10747.9
        'minimum': None,
        'maximum': None,
        'description': u"ACK of media on unload lane",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_UPSIDE_DOWN_EXTRACTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10705, 0x0003)],  # D10705/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be extracted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_UPSIDE_DOWN_INSERTION",
        'readonly': False,
        'priority': 1,
        'addresses': [(10708, 0x0003)],  # D10708/~14
        'minimum': None,
        'maximum': None,
        'description': u"If the plate while must be inserted upside down (value 2) or not (value 3)",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_PLATE_ABSENT_IN_CAROUSEL",
        'readonly': True,
        'priority': 10,
        'addresses': [(15006, 0x0080)],  # D15006.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel",
        'active': True
    }, {
        'name': "WL_FEAT_INC_3_PLATE_ABSENT_IN_CAROUSEL_ACK",
        'readonly': True,
        'priority': 10,
        'addresses': [(10747, 0x0080)],  # D10747.7
        'minimum': None,
        'maximum': None,
        'description': u"The requested plate is not present in the carousel ACK",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_ABSENT_PLATE_SUBPOSITION",
        'readonly': True,
        'priority': 10,
        'addresses': [(15007, 0xFFFF)],  # D15007
        'minimum': None,
        'maximum': None,
        'description': u"Subposition of the absent plate requested in the carousel",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_IMAGING_ALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0010)],  # D10747.4
        'minimum': None,
        'maximum': None,
        'description': u"Generic alarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_IMAGING_PREALARM",
        'readonly': False,
        'priority': 10,
        'addresses': [(10747, 0x0020)],  # D10747.5
        'minimum': None,
        'maximum': None,
        'description': u"Generic prealarm by the imaging",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_BUZZER_STATUS",
        'readonly': True,
        'priority': 10,
        'addresses': [(15006, 0x0040)],  # D15006.6
        'minimum': None,
        'maximum': None,
        'description': u"Status of the buzzer",
        'active': True
    },{
        'name': "WL_FEAT_INC_3_RESET_PLC_PLATES_MEMORY",
        'readonly': False,
        'priority': 10,
        'addresses': [(10746, 0x0200)],  # D10746.9
        'minimum': None,
        'maximum': None,
        'description': u"Reset the plc's memory of all incubated plates",
        'active': True
    }]
