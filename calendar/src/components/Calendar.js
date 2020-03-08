import React from 'react';
import "./Calendar.css";
import {format, addMonths, subMonths, startOfWeek, addDays,
         startOfMonth, endOfMonth, endOfWeek, isSameDay, isSameMonth} from "date-fns";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Modal from 'react-bootstrap/Modal';


export default class Planner extends React.Component {

    constructor(props) {
        super(props)
        this.apiEndpoint = props.apiEndpoint
        this.state = {    
            doctors: [],
            DoctorEvents: {},
            selectedDoctorId: null
        }
    }

    componentDidMount(){
      this.init_doctors();
    }

    render() {
        return (
            <Row>
              <Col>
                  {this.renderDocView()}
              </Col>
              <Col>
                  {this.renderEvents()}
              </Col>
            </Row>

        );
    }


    renderDocView() {
      let temp = []
        for (let i = 0; i < this.state.doctors.length; i++){
          let curr = this.state.doctors[i]
          temp.push(
          <Row key={curr.id}>
            <Col onClick = {() => this.getEventInfo(curr.id) }>
              {curr.doctor_last + ", " + curr.doctor_first}
            </Col>
          </Row>)
        }
        return temp
      }
    
      getEventInfo(curr_id){
        fetch(this.apiEndpoint + "physician_events"+"?id=" + curr_id.toString(), {mode: 'cors'})
        .then(res => res.json())
        .then((data) => {
          
          let events = data.data;
          let last = this.state.DoctorEvents

          last[curr_id] = events
          this.setState({DoctorEvents: last, selectedDoctorId: curr_id})
        })
        .catch(console.log)
      }

      renderEvents(){
        if (this.state.selectedDoctorId !== null){
          let temp = []

          let currEvents = this.state.DoctorEvents[this.state.selectedDoctorId];
          
            return (
              <Row >
                <Col>
                  {currEvents}
                </Col>
              </Row>
            )
          }
          return <div/>
        
      }



      init_doctors(){
        fetch(this.apiEndpoint + "physicians", {mode: 'cors'})
        .then(res => res.json())
        .then((data) => {
          let res = []
          let doctors = data.data;
          for (let i = 0; i < doctors.length; i++){
            res.push(doctors[i]);
          }
          console.log(res);
          this.setState({doctors: res})
        })
        .catch(console.log)
      }
}




