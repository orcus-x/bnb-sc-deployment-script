
# Smart Contract Deployment Script

This project contains a Python script, `deploy.py`, designed to deploy smart contracts to the Binance Smart Chain (BSC) Testnet using Web3.py.

## Features

- Connects to the BSC Testnet using a specified RPC URL.
- Reads the contract's ABI and bytecode files.
- Deploys the contract and returns the deployed contract address.
- Ensures secure and reliable transaction signing and broadcasting.

## Prerequisites

- Python 3.7+
- Web3.py (`pip install web3`)
- Access to the BSC Testnet RPC URL
- Contract ABI (`<contract_name>.abi`) and Bytecode (`<contract_name>.bin`) files

## Files

- `deploy.py`: The main script for deploying smart contracts.
- `<contract_name>.abi`: The ABI file of the contract to deploy.
- `<contract_name>.bin`: The bytecode file of the contract.

## How to Use

1. Clone the repository and navigate to the project directory.

2. Install dependencies:
   ```bash
   pip install web3
   ```

3. Prepare the ABI and Bytecode files of your smart contract in the same directory as the script.

4. Run the script with the following command:
   ```bash
   python deploy.py <contract_name> <private_key>
   ```
   Replace:
   - `<contract_name>` with the base name of your ABI and Bytecode files (without extensions).
   - `<private_key>` with your private key for signing transactions.

## Example

To deploy a contract named `MyContract`, use:
```bash
python deploy.py MyContract 0xYourPrivateKeyHere
```

## Output

- The script will print the following:
  - Address of the account deploying the contract.
  - Transaction hash of the deployment transaction.
  - Address of the deployed contract.

## Important Notes

- **Security**: Keep your private key secure. Avoid hardcoding it in the script.
- **Testnet Usage**: This script is configured for the BSC Testnet (chainId `97`). Modify the configuration for mainnet or other testnets if needed.
- **Gas Fees**: Ensure the account has enough test BNB to cover transaction fees.

## Disclaimer

This script is provided for educational purposes only. Use it at your own risk. The author is not responsible for any loss or damage caused by its use.

## License

This project is licensed under the MIT License.
