// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract VotingSystem {
    using SafeMath for uint256;

    struct Candidate {
        string name;
        uint256 voteCount;
    }

    struct Voter {
        bool registered;
        bool voted;
        uint256 candidateIndex;
    }

    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    address public owner;
    uint256 public votingStartTime;
    uint256 public votingEndTime;

    constructor(string[] memory _candidateNames, uint256 _votingDuration) {
        owner = msg.sender;
        votingStartTime = block.timestamp;
        votingEndTime = votingStartTime.add(_votingDuration);

        for (uint256 i = 0; i < _candidateNames.length; i++) {
            candidates.push(Candidate({
                name: _candidateNames[i],
                voteCount: 0
            }));
        }
    }

    function registerVoter(address _voter) public onlyOwner {
        require(!voters[_voter].registered, "Voter already registered.");
        
        voters[_voter].registered = true;
    }

    function vote(uint256 _candidateIndex) public {
        require(voters[msg.sender].registered, "Voter not registered.");
        require(!voters[msg.sender].voted, "Voter already voted.");
        require(_candidateIndex < candidates.length, "Invalid candidate index.");
        require(block.timestamp >= votingStartTime && block.timestamp <= votingEndTime, "Voting period has ended.");

        voters[msg.sender].voted = true;
        voters[msg.sender].candidateIndex = _candidateIndex;

        candidates[_candidateIndex].voteCount++;
    }

    function getCandidateCount() public view returns (uint256) {
        return candidates.length;
    }

    function getCandidateVoteCount(uint256 _candidateIndex) public view returns (uint256) {
        require(_candidateIndex < candidates.length, "Invalid candidate index.");
        
        return candidates[_candidateIndex].voteCount;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can perform this action.");
        _;
    }
}
