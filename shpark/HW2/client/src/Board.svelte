<script lang="ts">
  import Square from "./Square.svelte";
  import { fly, fade } from "svelte/transition";
  import * as d3 from "d3";
  import {onMount} from 'svelte'

  export let username: string;
  export let winRate: Object;

  let histories = [
    {
      OXs: Array(9).fill(null),
    },
  ];
  let stepNumber: number = 0;
  let xIsNext: boolean = true;

  let current = histories[stepNumber];
  let winner = calculateWinner(current.OXs);
  let playing: boolean = false;

  function onClick(i: number) {
    if (!playing) {
      console.log(histories);
      playing = true;
      const history = histories.slice(0, stepNumber + 1);
      const current = history[history.length - 1];
      const OXs = current.OXs.slice();

      if (calculateWinner(OXs) || OXs[i]) {
        return;
      }

      OXs[i] = xIsNext ? "X" : "O";
      histories = history.concat([
        {
          OXs: OXs,
        },
      ]);
      stepNumber = history.length;
      xIsNext = !xIsNext;

      update();

      if (calculateWinner(OXs)) {
        // winner 전적 기록하기
        return;
      }

      var request = new XMLHttpRequest();
      request.open("POST", "http://0.0.0.0:8080/next", true);
      request.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
      );
      // request.responseType = 'json';
      console.log(OXs);
      request.send(OXs.toString());

      request.onreadystatechange = () => {
        if (request.readyState == 4) {
          if (request.status == 200) {
            setTimeout(() => {
              console.log(request.responseText);

              OXs[request.responseText] = xIsNext ? "X" : "O";
              histories = history.concat([
                {
                  OXs: OXs,
                },
              ]);
              stepNumber = history.length;
              xIsNext = !xIsNext;
              update();
              playing = false;
              
            }, 1000);
          } else {
            alert("error code: " + request.status);
          }
        }
      };
    }
  }

  function moveTo(i: number) {
    stepNumber = i;
    xIsNext = stepNumber % 2 === 0;
    update();
    playing = false;
  }

  function calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (
        squares[a] &&
        squares[a] === squares[b] &&
        squares[b] === squares[c] &&
        squares[c]
      ) {
        return squares[a];
      }
    }

    if (!squares.includes(null)) {
      return "draw";
    }

    return null;
  }

  function update() {
    current = histories[stepNumber];
    winner = calculateWinner(current.OXs);
    if (winner != null) {
      chartupdate(winner)
    }
  }

  var dataset = [winRate.win, winRate.draw, winRate.lose];

  var width = 200,
    height = 200,
    radius = 150;

  var color = ["#00DDFF", "#FFF6B5", "#F75990"];

  let piediv;

  var svg = d3
    .select('body')
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  function render(data) {
    var pie = d3.pie().sort(null);

    var arc = d3
      .arc()
      .innerRadius(radius - 100)
      .outerRadius(radius - 50);

    var path = svg.selectAll("path").data(pie(data));

    var pathEnter = path
      .enter()
      .append("path")
      .attr("fill", function (d, i) {
        return color[i];
      })
      .attr("d", arc);

    var path = path.attr("d", arc);
  }

  render(dataset);

  function chartupdate(winner) {
    console.log('chartupdate')
    var request = new XMLHttpRequest();
    request.open("POST", "http://0.0.0.0:8080/update", true);
    request.setRequestHeader(
      "Content-Type",
      "application/x-www-form-urlencoded"
    );
    // request.responseType = 'json';
    var result = new Object();
    result.username = username;
    result.winner = winner;
    console.log(result)
    request.send(JSON.stringify(result));

    request.onreadystatechange = () => {
        if (request.readyState == 4) {
          if (request.status == 200) {
            let userHistory = JSON.parse(request.responseText);
            winRate = userHistory;
            dataset = [winRate.win, winRate.draw, winRate.lose];
            console.log(userHistory)
            console.log(winRate)
            console.log(dataset)
            render(dataset);
          } else {
            alert("error code: " + request.status);
          }
        }
      };


  }
</script>

<style>
  .board {
    position: relative;
    padding: 2em;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .row {
    float: left;
  }
  .console {
    float: left;
  }
</style>

<div class="console">
  <div class="board">
    {#each current.OXs as OX, i}
      <div class="row">
        <Square value={OX} onClick={() => onClick(i)} />
      </div>
      {#if (i + 1) % 3 == 0}
        <div />
      {/if}
    {/each}
  </div>

  <div>

    {#if !winner}
      Next Player
      {#if xIsNext}
        <p in:fade={{ duration: 500 }}>X</p>
      {:else}
        <p in:fade={{ duration: 500 }}>O</p>
      {/if}
    {:else}
      Winner
      <p in:fade={{ duration: 500 }}>{winner}</p>
    {/if}
    <button on:click={() => moveTo(0)}>Go to game start</button>
    
  </div>

  <!-- {#each histories as _, i}
      {#if i == 0} -->
  <!-- <li in:fly={{ y: 20, duration: 500 }} out:fade> -->
  <!-- </li> -->
  <!-- {:else}
        <li in:fly={{ y: 20, duration: 500 }} out:fade>
          <button on:click={() => moveTo(i)}>Go to move #{i}</button>
        </li>
      {/if}
    {/each} -->
</div>
<div>{username}</div>
    {winRate.win}승
    {winRate.draw}무
    {winRate.lose}패
    <div bind:this={piediv}></div>