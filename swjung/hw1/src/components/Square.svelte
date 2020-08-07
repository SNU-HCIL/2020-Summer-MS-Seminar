<style>
    .square {
        background: #fff;
        border: 1px solid #999;
        float: left;
        font-size: 24px;
        font-weight: bold;
        line-height: 34px;
        height: 34px;
        margin-right: -1px;
        margin-top: -1px;
        margin-bottom: -1px;
        padding: 0px;
        text-align: center;
        width: 34px;
    }

    .square:focus {
        outline: none;
    }
</style>
<script lang='ts'>
    import {createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();
    export let value = '';
    export let index = null;
    //export let id = null;
    let handleClick = (e) => {
        dispatch('click', {
            index: index,
        });
    }
</script>


<button 
    class='square'
    on:click={handleClick}>
    {value}
    </button>
