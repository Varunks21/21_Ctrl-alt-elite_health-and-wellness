// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public data;

    // Function to set the value of data
    function set(uint256 _data) public {
        data = _data;
    }

    // Function to get the value of data
    function get() public view returns (uint256) {
        return data;
    }
}