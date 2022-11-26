<template>
    <div class="container">
        <div class="columns is-multiline">
            <img src="@/assets/games.png" width="150" height="83px">
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Game</th>
                            <th>Played On</th>
                        </tr>
                    </thead>
                    <tbody>
                    <!-- For each game, display the id with a router link, as well as the date played !-->
                        <tr
                            v-for="game in game"
                            v-bind:key="game.id">
                                <td><router-link :to="{ name: 'Game', params: { id: game.id}}">{{game.id}}</router-link></td>
                                <td>{{ game.date.split('T')[0] }}</td>
                                <td></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default { 
        name: 'Games',
        data() { 
            return { 
                game: [],
            }
        },
        mounted() { 
            this.getGame()
        },
        methods: { 
            async getGame() { 
                this.$store.commit('setIsLoading', true)
                axios
                    .get('/api/v1/games/')
                    .then(response => { 
                        this.game = response.data.reverse()
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>