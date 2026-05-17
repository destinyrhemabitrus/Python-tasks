""" Nokia3310 """

"""print("--MAIN MENU--\n\n1.Phone book\n2.Messages\n3.Chat\n4.Call register\n5.Tones\n6.Settings\n"
                        +   "7.Call divert\n8.Games\n9.Calculator\n10.Reminders\n11.Clock\n12.Profiles\n13.Sim services\n0.Exit\n\n")"""

main_menu = True

while main_menu:
    print("--MAIN MENU--\n\n1.Phone book\n2.Messages\n3.Chat\n4.Call register\n5.Tones\n6.Settings\n"
                        +   "7.Call divert\n8.Games\n9.Calculator\n10.Reminders\n11.Clock\n12.Profiles\n13.Sim services\n0.Exit\n\n")
    main_menuChoice = input()

    match main_menuChoice:

        case "1":
            phone_book = True

            while phone_book:
                print("--Phone book--\n1.Search\n2.Service Nos\n3.Add name\n4.Erase\n5.Edit\n6.Assign tone\n7.Send b'card\n"
                                +   "8.Options\n9.Speed dial\n10.Voice tags\n0.Back\n\n")
                phone_bookChoice = input()
                
                match phone_bookChoice:
                
                    case "1":
                        print("--Search--\n0.Back\n\n");


                    case "2":
                        print("--Service Nos'--\n0.Back\n\n")


                    case "3":
                        print("--Add name--\n0.Back\n\n")


                    case "4":
                        print("--Erase'--\n0.Back\n\n")


                    case "5":
                        print("--Edit--\n0.Back\n\n")


                    case "6":
                        print("--Assign tone'--\n0.Back\n\n")


                    case "7":
                        print("--Send b'card'--\n0.Back\n\n")


                    case "8":
                        option = True

                        while option:
                            print("--Options--\n1.Type of view\n2.Memory status\n0.Back\n\n")
                            optionChoice = input()
                
                            match optionChoice:

                                case "1":
                                    print("--Type of view--\n0.Back\n\n")


                                case "2":
                                    print("--Memory status--\n0.Back\n\n")


                                case "0":
                                    option = False


                                case _:
                                    print("Invalid selection\n")            


                    case "9":
                        print("--Speed dial--\n0.Back\n\n")


                    case "10":
                        print("--Voice tags--\n0.Back\n\n")


                    case "0":
                        phone_book = False


                    case _:
                        print("Invalid selection\n")            

                            
        #Case 2 of Main menu
        case "2":
            messages = True

            while messages:
                print("--Messages--\n1.Write messages\n2.Inbox\n3.Outbox\n4.Picture messages\n5.Templetes\n6.Smileys\n7.Message settings\n"
                                +   "8.Info service\n9.Voice mailbox number\n10.Service command editor\n0.Back\n\n")
                messages_choice = input()
                
                match messages_choice: 

                    case "1":
                        print("--Write messages--\n0.Back\n\n")


                    case "2":
                        print("--Inbox--\n0.Back\n\n")


                    case "3":
                        print("--Outbox--\n0.Back\n\n")


                    case "4":
                        print("--Picture messages--\n0.Back\n\n")


                    case "5":
                        print("--Templetes--\n0.Back\n\n")


                    case "6":
                        print("--Smileys--\n0.Back\n\n")


                    case "7":
                        message_settings = True

                        while message_settings:
                            print("--Message settings--\n1.Set 1\n2.Common\n0.Back\n\n")
                            message_settingsChoice = input()

                            match message_settingsChoice:

                                case "1":
                                    set_1 = True
                                    
                                    while set_1:
                                        print("--Set 1--\n1.Message center number\n2.Message sent as\n3.Message validity\n0.Back\n\n")
                                        set1_choice = input()

                                        match set1_choice:
                                        
                                            case "1":
                                                print("--Message center number--\n0.Back\n\n")


                                            case "2":
                                                print("--Message sent as--\n0.Back\n\n")


                                            case "3":
                                                print("--Message validity--\n0.Back\n\n")


                                            case "0":
                                                set_1 = False


                                            case _:
                                                print("Invalid selection\n")
        

                                case "2":
                                    common = True
                                
                                    while common:
                                        print("--Common--\n1.Deliver reports\n2.Reply via same centre\n3.Character support\n0.Back\n\n");
                                        common_choice = input()

                                        match common_choice:
                                        
                                            case "1":
                                                print("--Deliver reports--\n0.Back\n\n")


                                            case "2":
                                                print("--Reply via same centre--\n0.Back\n\n")


                                            case "3":
                                                print("--Character support--\n0.Back\n\n")


                                            case "0":
                                                common = False

                                        
                                            case _:
                                                print("Invalid selection\n")



                                case "0":
                                    message_settings = False


                                case _:
                                    print("Invalid selection\n")            



                    case "8":
                        print("--Info service--\n0.Back\n\n")


                    case "9":
                        print("--Voice mailbox number--\n0.Back\n\n")


                    case "10":
                        print("--Service command editor--\n0.Back\n\n")


                    case "0":
                        messages = False


                    case _:
                        print("Invalid selection\n")            



        case "3":
            print("--Chat--\n0.Back\n\n")

        
        case "4":
            call_register = True

            while call_register:
                print("--Call register--\n1.Missed calls\n2.Received calls\n3.Dialled calls\n4.Erase recent call lists\n5.Show call duration\n6.Show call costs\n7.Call costs settings\n"
                                +   "8.Prepared credit\n0.Back\n\n")
                call_registerChoice = input()

                match call_registerChoice:
            
                    case "1":
                        print("--Missed calls--\n0.Back\n\n")


                    case "2":
                        print("--Received calls--\n0.Back\n\n")


                    case "3":
                        print("--Dialled calls--\n0.Back\n\n")


                    case "4":
                        print("--Erase recent call lists--\n0.Back\n\n")


                    case "5":
                        call_duration = True

                        while call_duration:
                            print("--Show call duration--\n1.Last call duration\n2.All calls' duration\n3.Received calls' duration\n4.Dialled calls' duration\n5.Clear timers\n0.Back\n\n")
                            call_durationChoice = input()
                                        
                            match call_durationChoice:
                            
                                case "1":
                                    print("--Last call duration--\n0.Back\n\n")


                                case "2":
                                    print("--All calls' duration--\n0.Back\n\n")


                                case "3":
                                    print("--Received calls' duration--\n0.Back\n\n")


                                case "4":
                                    print("--Dialled calls' duration--\n0.Back\n\n")


                                case "5":
                                    print("--Clear timers--\n0.Back\n\n")


                                case "0":
                                    call_duration = False


                                case _:
                                    print("Invalid selection\n") 


                    case "6":
                        print("--Show call costs--\n0.Back\n\n")


                    case "7":
                        print("--Call costs settings--\n0.Back\n\n")


                    case "8":
                        print("--Prepared credit--\n0.Back\n\n")


                    case "0":
                        call_register = False


                    case _:
                        print("Invalid selection\n") 


        case "5":
            print("--Tones--\n1.Ringing tone\n2.Ringing volume\n3.Incoming call alert\n4.Composer\n5.Message alert tone\n6.Keypad tones\n7.Warning and game tones\n"
                            +   "8.Vibrating alert\n9.Screen saver\n0.Back\n\n")


        case "6":
            print("--Settings--\n1.Call settings\n2.Phone settings\n3.Security settings\n4.Restore factory settings\n0.Back\n\n")


        case "7":
            print("--Call divert--\n0.Back\n\n")


        case "8":
            print("--Games--\n0.Back\n\n")


        case "9":
            print("--Calculator--\n0.Back\n\n")


        case "10":
            print("--Reminders--\n0.Back\n\n")


        case "11":
            print("--Clock--\n1.Alarm clock\n2.Clock settings\n3.Date setting\n4.Stopwatch\n5.Countdown timer\n6.Auto update of date and time\n0.Back\n\n");


        case "12":
            print("--Profiles--\n0.Back\n\n")


        case "13":
            print("--SIM services--\n0.Back\n\n")


        case "0":
            main_menu = False


        case _:
            print("Invalid selection\n")            


  
