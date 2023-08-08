import csv


def csv_to_qif(csv_file_path, qif_file_path, completion_status='COMPLETE'):
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        with open(qif_file_path, 'w') as qif_file:
            qif_file.write('!Type:Invst\n')

            for row in csv_reader:
                date = row['trade_date']
                tran_mode = row['transaction_mode']
                scheme = row['scheme_name']
                nav = float(row['nav'])
                units = float(row['units'])
                amount = int(row['amount'])
                commission = amount-(units*nav)
                exchange_order_id = row['exchange_order_id']
                completion = row['status'].strip().lower()

                if completion == completion_status.lower():
                    qif_file.write(f'D{date}\n')
                    qif_file.write(f'N{tran_mode}\n')
                    qif_file.write(f'Y{scheme}\n')
                    qif_file.write(f'I{nav:.2f}\n')
                    qif_file.write(f'Q{units:.3f}\n')
                    qif_file.write(f'U{amount:}\n')
                    qif_file.write(f'T{amount:}\n')
                    qif_file.write(f'O{commission:.2f}\n')
                    qif_file.write(f'M{exchange_order_id}\n')
                    qif_file.write(f'^\n')

            print(f'Conversion completed. QIF file saved to {qif_file_path}')


if __name__ == "__main__":
    csv_file_path = input("Enter the path to the CSV file: ")
    qif_file_path = input("Enter the path to save the QIF file: ")

    csv_to_qif(csv_file_path, qif_file_path)
