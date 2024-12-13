<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            People and Their Motorbikes
        </div>

        <!-- Bootstrap Tabs for Models -->
        <ul class="nav nav-tabs mb-3">
            <li class="nav-item">
                <a class="nav-link active" data-bs-toggle="tab" href="#persons">Persons</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#motorbikes">Motorbikes</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#rides">Rides</a>
            </li>
        </ul>

        <div class="tab-content">
            <!-- Person Table -->
            <div class="tab-pane fade show active" id="persons">
                <button class="btn btn-success btn-sm mb-3" data-bs-toggle="modal" data-bs-target="#addPersonModal">
                    <i class="bi bi-plus"></i> Add Person
                </button>
                <PersonTable 
                    :persons="persons" 
                    @delete-person="deletePerson"
                    @edit-person="openEditPerson"
                />
            </div>

            <!-- Motorbike Table -->
            <div class="tab-pane fade" id="motorbikes">
                <button class="btn btn-success btn-sm mb-3" data-bs-toggle="modal" data-bs-target="#addMotorbikeModal">
                    <i class="bi bi-plus"></i> Add Motorbike
                </button>
                <MotorbikeTable 
                    :motorbikes="motorbikes" 
                    @delete-motorbike="deleteMotorbike"
                    @edit-motorbike="openEditMotorbike"
                />
            </div>

            <!-- Ride Table -->
            <div class="tab-pane fade" id="rides">
                <button class="btn btn-success btn-sm mb-3" data-bs-toggle="modal" data-bs-target="#addRideModal">
                    <i class="bi bi-plus"></i> Add Ride
                </button>
                <RideTable 
                    :rides="rides" 
                    @delete-ride="deleteRide"
                    @edit-ride="openEditRide"
                />
            </div>
        </div>

        <!-- Add Person Modal -->
        <div class="modal fade" id="addPersonModal" tabindex="-1" aria-labelledby="addPersonModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addPersonModalLabel">Add Person</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="newPerson.name" type="text" class="form-control" placeholder="Name" />
                        <input v-model="newPerson.date_of_birth" type="date" class="form-control mt-2" placeholder="Date of Birth" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createPerson" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Motorbike Modal -->
        <div class="modal fade" id="addMotorbikeModal" tabindex="-1" aria-labelledby="addMotorbikeModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addMotorbikeModalLabel">Add Motorbike</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="newMotorbike.name" type="text" class="form-control" placeholder="Name" />
                        <input v-model="newMotorbike.engine_capacity" type="number" class="form-control mt-2" placeholder="Engine Capacity" />
                        <textarea v-model="newMotorbike.description" class="form-control mt-2" placeholder="Description"></textarea>
                        <div class="form-check mt-2">
                            <input v-model="newMotorbike.is_automatic" type="checkbox" class="form-check-input" id="isAutomatic" />
                            <label class="form-check-label" for="isAutomatic">Automatic</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createMotorbike" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Ride Modal -->
        <div class="modal fade" id="addRideModal" tabindex="-1" aria-labelledby="addRideModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addRideModalLabel">Add Ride</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <select v-model="newRide.person_id" class="form-control">
                            <option v-for="person in persons" :value="person.id">{{ person.name }}</option>
                        </select>
                        <select v-model="newRide.motorbike_id" class="form-control mt-2">
                            <option v-for="motorbike in motorbikes" :value="motorbike.id">{{ motorbike.name }}</option>
                        </select>
                        <div class="form-check mt-2">
                            <input v-model="newRide.is_favourite" type="checkbox" class="form-check-input" id="isFavourite" />
                            <label class="form-check-label" for="isFavourite">Favourite</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createRide" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Person Modal -->
        <div class="modal fade" id="editPersonModal" tabindex="-1" aria-labelledby="editPersonModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editPersonModalLabel">Edit Person</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="editedPerson.name" type="text" class="form-control" placeholder="Name" />
                        <input v-model="editedPerson.date_of_birth" type="date" class="form-control mt-2" placeholder="Date of Birth" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updatePerson" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Motorbike Modal -->
        <div class="modal fade" id="editMotorbikeModal" tabindex="-1" aria-labelledby="editMotorbikeModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editMotorbikeModalLabel">Edit Motorbike</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="editedMotorbike.name" type="text" class="form-control" placeholder="Name" />
                        <input v-model="editedMotorbike.engine_capacity" type="number" class="form-control mt-2" placeholder="Engine Capacity" />
                        <textarea v-model="editedMotorbike.description" class="form-control mt-2" placeholder="Description"></textarea>
                        <div class="form-check mt-2">
                            <input v-model="editedMotorbike.is_automatic" type="checkbox" class="form-check-input" id="editIsAutomatic" />
                            <label class="form-check-label" for="editIsAutomatic">Automatic</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateMotorbike" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Ride Modal -->
        <div class="modal fade" id="editRideModal" tabindex="-1" aria-labelledby="editRideModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editRideModalLabel">Edit Ride</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <select v-model="editedRide.person_id" class="form-control">
                            <option v-for="person in persons" :key="person.id" :value="person.id">{{ person.name }}</option>
                        </select>
                        <select v-model="editedRide.motorbike_id" class="form-control mt-2">
                            <option v-for="motorbike in motorbikes" :key="motorbike.id" :value="motorbike.id">{{ motorbike.name }}</option>
                        </select>
                        <div class="form-check mt-2">
                            <input v-model="editedRide.is_favourite" type="checkbox" class="form-check-input" id="editIsFavourite" />
                            <label class="form-check-label" for="editIsFavourite">Favourite</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateRide" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </div>  
</template>


<script>
import PersonTable from './components/PersonTable.vue'
import MotorbikeTable from './components/MotorbikeTable.vue'
import RideTable from './components/RideTable.vue'

const baseUrl = 'http://localhost:8000'

export default {
    components: {
        PersonTable,
        MotorbikeTable,
        RideTable
    },
    data() {
        return {
            persons: [],
            motorbikes: [],
            rides: [],
            newPerson: { name: '', date_of_birth: '' },
            newMotorbike: { name: '', engine_capacity: 0, description: '', is_automatic: false },
            newRide: { person_id: null, motorbike_id: null, is_favourite: false },
            editedPerson: {}, 
            editedMotorbike: {},
            editedRide: {}
        }
    },  

    async mounted() {
        const personResponse = await fetch(`${baseUrl}/api/persons/`)
        this.persons = await personResponse.json()

        const motorbikeResponse = await fetch(`${baseUrl}/api/motorbikes/`)
        this.motorbikes = await motorbikeResponse.json()

        const rideResponse = await fetch(`${baseUrl}/api/rides/`)
        this.rides = await rideResponse.json()
    },
    methods: {

        async createPerson() {
            const response = await fetch(`${baseUrl}/api/persons/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newPerson)
            });
            const newPerson = await response.json();
            this.persons.push(newPerson);
            this.newPerson = { name: '', date_of_birth: '' };
        },
        async createMotorbike() {
            const response = await fetch(`${baseUrl}/api/motorbikes/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newMotorbike)
            });
            const newMotorbike = await response.json();
            this.motorbikes.push(newMotorbike);
            this.newMotorbike = { name: '', engine_capacity: 0, description: '', is_automatic: false };
        },
        async createRide() {
            try { 
                const response = await fetch(`${baseUrl}/api/rides/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newRide)
                });
                const newRide = await response.json();
                this.rides.push(newRide);
                this.newRide = { person_id: null, motorbike_id: null, is_favourite: false };
            } catch(error) { 
                console.error("Error in createRide:", error);
                alert("Failed to add ride. Please check the console for more details.");
            }
        },
        async deletePerson(person) {
            if (confirm(`Are you sure you want to delete person '${person.name}'?`)) {
                const response = await fetch(`${baseUrl}/api/person/${person.id}/`, {
                    method: 'DELETE',
                });

                if (response.ok) {
                    this.persons = this.persons.filter(p => p.id !== person.id);
                }
            }
        },


        async deleteMotorbike(motorbike) {
            if (confirm(`Are you sure you want to delete motorbike '${motorbike.name}'?`)) {
                try {
                    const response = await fetch(`${baseUrl}/api/motorbike/${motorbike.id}/`, {
                        method: 'DELETE',
                    });
                    if (!response.ok) throw new Error(`Failed to delete motorbike: ${response.statusText}`);
                    this.motorbikes = this.motorbikes.filter(m => m.id !== motorbike.id);
                    this.rides = this.rides.filter(ride => ride.motorbike_id !== motorbike.id);
                } catch (error) {
                    console.error("Error in deleteMotorbike:", error);
                    alert("Failed to delete motorbike. Please check the console for more details.");
                }
            }
        },
        async deleteRide(ride) {
            if (confirm(`Are you sure you want to delete this ride?`)) {
                try {
                    const response = await fetch(`${baseUrl}/api/rides/${ride.id}/`, {
                        method: 'DELETE',
                    });
                    if (!response.ok) throw new Error(`Failed to delete ride: ${response.statusText}`);
                    this.rides = this.rides.filter(r => r.id !== ride.id);
                } catch (error) {
                    console.error("Error in deleteRide:", error);
                    alert("Failed to delete ride. Please check the console for more details.");
                }
            }
        },

        openEditPerson(person) {
            console.log('openEditPerson called with:', person);
            this.editedPerson = { ...person };

            import('bootstrap').then(bootstrap => {
                const modal = new bootstrap.Modal(document.getElementById('editPersonModal'));
                modal.show();
            }).catch(error => {
                console.error('Error loading Bootstrap:', error);
            });
        },



        openEditMotorbike(motorbike) {
        console.log('openEditMotorbike called with:', motorbike);
        this.editedMotorbike = { ...motorbike };
    
        import('bootstrap').then(bootstrap => {
            const modal = new bootstrap.Modal(document.getElementById('editMotorbikeModal'));
            modal.show();
        }).catch(error => {
            console.error('Error loading Bootstrap:', error);
            });
        },

        async updateMotorbike() {
        try {
            const response = await fetch(`${baseUrl}/api/motorbike/${this.editedMotorbike.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.editedMotorbike)
            });

            if (!response.ok) throw new Error(`Failed to update motorbike: ${response.statusText}`);
            
            const updatedMotorbike = await response.json();

            this.motorbikes = this.motorbikes.map(motorbike => 
                motorbike.id === updatedMotorbike.id ? updatedMotorbike : motorbike
            );
        } catch (error) {
            console.error("Error updating motorbike:", error);
            alert("Failed to update motorbike. Please check the console for more details.");
            }
        },

        async updatePerson() {
            try {
                const response = await fetch(`${baseUrl}/api/person/${this.editedPerson.id}/`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.editedPerson)
                });

                if (!response.ok) throw new Error(`Failed to update person: ${response.statusText}`);
                
                const updatedPerson = await response.json();
                this.persons = this.persons.map(person =>                                                                                                                                                                                                                                                                                                                                                                  
                    person.id === updatedPerson.id ? updatedPerson : person
                );
            } catch (error) {
                console.error("Error updating person:", error);
                alert("Failed to update person. Please check the console for more details.");
            }
        },

        openEditRide(ride) {
            console.log('openEditRide called with:', ride);
            this.editedRide = {
                id: ride.id,
                person_id: ride.person_id,
                motorbike_id: ride.motorbike_id,
                is_favourite: ride.is_favourite
            };

            import('bootstrap').then(bootstrap => {
                const modal = new bootstrap.Modal(document.getElementById('editRideModal'));
                modal.show();
            }).catch(error => {
                console.error('Error loading Bootstrap:', error);
            });
        },


        async updateRide() {
            try {
                const response = await fetch(`${baseUrl}/api/rides/${this.editedRide.id}/`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.editedRide)
                });

                if (!response.ok) throw new Error(`Failed to update ride: ${response.statusText}`);
                await this.fetchRides(); //

            } catch (error) {
                console.error("Error updating ride:", error);
                alert("Failed to update ride. Please check the console for more details.");
            }
        },

        async fetchRides() {
            const rideResponse = await fetch(`${baseUrl}/api/rides/`);
            this.rides = await rideResponse.json();
        }

    }
}
</script>

<style scoped>
</style>
