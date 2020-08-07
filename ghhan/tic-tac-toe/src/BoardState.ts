export class BoardState{
    cells: Array<string>;
    turnOfTheFirst: boolean;
    constructor(public w: number, public h: number){
        this.cells = new Array(w * h).fill('')
        this.turnOfTheFirst = true
    }
}
