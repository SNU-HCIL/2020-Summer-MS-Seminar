<script lang="ts">
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { idStore } from "./stores"
    import { winStore, loseStore, drawStore } from "./stores"
    import axios from 'axios'

    let x = 100;
    let y = 100;

    let status : string = "";

    let svg;
    let pies;
    let text;

    let win : number;
    let lose : number;
    let draw : number;

    interface WDL {
        win : number,
        draw : number,
        lose : number,
        spare : number,
    }

    let currentStatus = null;


    let colors = ["#8ec0fa", "#ff6f69", "#81C784", "#888888"];

    let id;
    
    let domain = "http://localhost:8000/login/";

    

    async function getStatus(id : string) {
        const response = await axios.get(domain + 'status/' + id);
        console.log(response);
        let spare : number = (response.data.win + response.data.draw + response.data.lose) > 0 ? 0 : 1;
        winStore.set(response.data.win);
        drawStore.set(response.data.draw);
        loseStore.set(response.data.lose);
        currentStatus = {
            win : win,
            lose : lose,
            draw : draw,
            spare : spare,
        };
    }


    function updateRecord() {
        let spare : number;
        if((win + lose + draw == 0)) spare = 1;
        else                         spare = 0;

        console.log(win, lose, draw, initial);
        currentStatus = {
            win : win,
            lose : lose,
            draw : draw,
            spare : spare,
        };

        let data = currentStatus;
        let statusStr : string = (Math.round((data.win * 100) / (data.lose + data.draw + data.win + data.spare))).toString() + "%";

        let pie = d3.pie()
                    .value(function(d) {return d.value; })
        let data_ready = pie(d3.entries(data))

        let color = d3.scaleOrdinal()
                      .domain(data)
                      .range(colors);

        pies.data(data_ready)
            .join(
                enter => enter.append('path')
                              .attr('d', d3.arc()
                                    .innerRadius(75)
                                    .outerRadius(100)
                               )
                                .attr('fill', function(d){ return(color(d.data.key)) }),
                update => update
                                .attr('d', d3.arc()
                                    .innerRadius(75)
                                    .outerRadius(100)
                                ),
            );

                  

        text.text(statusStr);

        // status
        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.lose.toString() + "L";

    }

    let initial : boolean;

    onMount(async () => {
        initial = true;

        // subscribe
        idStore.subscribe( v => { id = v; } )
        winStore.subscribe( v => {
            win = v;
            if (!initial) updateRecord();
        })
        loseStore.subscribe( v => {
            lose = v;
            if (!initial) updateRecord();
        })
        drawStore.subscribe( v => {
            draw = v;
            if (!initial) updateRecord();
        })


        await getStatus(id);

        svg = d3.select("#record-svg")
                .append('g')
                .attr("transform", "translate(" + x + "," + y + ")");

        let data = currentStatus;

        let statusStr : string = (Math.round((data.win * 100) / (data.lose + data.draw + data.win + data.spare))).toString() + "%"
        let color = d3.scaleOrdinal()
                      .domain(data)
                      .range(colors);

        // Compute the position of each group on the pie:
        let pie = d3.pie()
                    .value(function(d) {return d.value; })
        let data_ready = pie(d3.entries(data))

        pies = svg.selectAll('path')
                  .data(data_ready)
                  .enter()
                  .append('path')
                  .attr('d', d3.arc()
                          .innerRadius(75)
                          .outerRadius(100)
                      )
                  .attr('fill', function(d){ return(color(d.data.key)) });

        text = svg.append("text")
                  .text(statusStr)
                  .attr("x", -15);

        // status
        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.lose.toString() + "L";


        // not initial
        initial = false;



    });




</script>



<div id="record-view">
    <h3>{status}</h3>
    <svg id="record-svg"></svg>
    <h4>signed in as {id}</h4>
</div>


<style>
    #record-view {
        display: block;
    }

    #record-svg {
        width: 200px;
        height: 200px;

    }

    h3 {
        color: #03254c;
		font-size: 1.5em;
        font-weight: 200;
        margin: 20px;
        margin-left: 25px;
        margin-top: 23px;
        margin-bottom: 15px;
        width: 200px;
    }

    h4 {
        color: #03254c;
		font-size: 1em;
        font-weight: 200;
        margin: 20px;
        margin-left: 25px;
        margin-top:14px;
        margin-bottom:9px;
        width: 200px;
    }

</style>