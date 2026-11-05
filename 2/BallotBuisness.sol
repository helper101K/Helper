// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Ballot {
    struct Vote {
        address voterAddress;
        bool choice;
    }

    struct Voter {
        string voterName;
        bool voted;
        bool registered;
    }

    enum State {
        Created,
        Voting,
        Ended
    }

    uint256 private countResult;
    uint256 public finalResult;
    uint256 public totalVoter;
    uint256 public totalVote;

    address public ballotOfficialAddress;
    string public ballotOfficialName;
    string public proposal;

    mapping(uint256 => Vote) private votes;
    mapping(address => Voter) public voterRegister;

    State public state;

    modifier condition(bool conditionValue) {
        require(conditionValue, "Condition is false");
        _;
    }

    modifier onlyOfficial() {
        require(
            msg.sender == ballotOfficialAddress,
            "Only the ballot official can call this"
        );
        _;
    }

    modifier inState(State expectedState) {
        require(state == expectedState, "Invalid ballot state");
        _;
    }

    constructor(
        string memory ballotOfficialNameValue,
        string memory proposalValue
    ) {
        ballotOfficialAddress = msg.sender;
        ballotOfficialName = ballotOfficialNameValue;
        proposal = proposalValue;
        state = State.Created;
    }

    function addVoter(address voterAddress, string memory voterName)
        public
        inState(State.Created)
        onlyOfficial
    {
        require(voterAddress != address(0), "Invalid voter address");
        require(bytes(voterName).length > 0, "Voter name is required");
        require(
            !voterRegister[voterAddress].registered,
            "Voter is already registered"
        );

        voterRegister[voterAddress] = Voter({
            voterName: voterName,
            voted: false,
            registered: true
        });
        totalVoter++;
    }

    function startVote() public inState(State.Created) onlyOfficial {
        require(totalVoter > 0, "Register at least one voter");
        state = State.Voting;
    }

    function doVote(bool choice)
        public
        inState(State.Voting)
        returns (bool)
    {
        Voter storage voter = voterRegister[msg.sender];
        require(voter.registered, "You are not a registered voter");
        require(!voter.voted, "You have already voted");

        voter.voted = true;
        votes[totalVote] = Vote({
            voterAddress: msg.sender,
            choice: choice
        });
        totalVote++;

        if (choice) {
            countResult++;
        }

        return true;
    }

    function endVote() public inState(State.Voting) onlyOfficial {
        state = State.Ended;
        finalResult = countResult;
    }

    function getVote(uint256 voteIndex)
        public
        view
        inState(State.Ended)
        returns (address, bool)
    {
        require(voteIndex < totalVote, "Vote index out of range");
        Vote memory vote = votes[voteIndex];
        return (vote.voterAddress, vote.choice);
    }

    function getRegisteredVoter(address voterAddress)
        public
        view
        returns (string memory, bool, bool)
    {
        Voter memory voter = voterRegister[voterAddress];
        return (voter.voterName, voter.voted, voter.registered);
    }
}
