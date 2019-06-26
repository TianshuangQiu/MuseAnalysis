import argparse
import math
import Analysis


def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))


def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
    except ValueError:
        pass


def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4, ch5, ch6):
    #print(unused_addr, args, "EEG (uV) per channel: ", ch1, ch2, ch3, ch4, ch5, ch6)
    Analysis.add(ch1, ch2, ch3, ch4, ch5)


def main():
    from pythonosc import dispatcher
    from pythonosc import osc_server
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/eeg", eeg_handler, "EEG")
    # dispatcher.map("/eeg",raw_printer)
    dispatcher.map("", print_volume_handler, "Volume")
    dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()


if __name__ == "__main__":
    main()
