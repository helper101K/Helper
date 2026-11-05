
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {

    address private accOwner;
    uint256 private balance = 0;

    constructor() {
        accOwner = msg.sender;
    }

    // Deposit money
    function Deposit() public payable {
        require(accOwner == msg.sender, "You are not an account owner!");
        require(msg.value > 0, "Amount should be greater than 0.");

        balance += msg.value;
    }

    // Withdraw money
    function Withdraw(uint256 amount) public {
        require(accOwner == msg.sender, "You are not an account owner!");
        require(amount > 0, "Amount should be greater than 0.");
        require(amount <= balance, "Insufficient balance!");

        // Update balance before transferring ETH
        balance -= amount;

        (bool success, ) = payable(accOwner).call{value: amount}("");

        require(success, "Withdrawal failed!");
    }

    // Show balance
    function showBalance() public view returns (uint256) {
        require(accOwner == msg.sender, "You are not an account owner!");

        return balance;
    }
}