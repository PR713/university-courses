import {useState} from "react";
import Dodawanie from "./Dodawanie.tsx";


interface Student {
    imie: string;
    nazwisko: string;
    rocznik: number;
}

const Students: Student[] = [{imie: "Jan", nazwisko: "Kowalski", rocznik: 2021},
    {imie: "Anna", nazwisko: "Nowak", rocznik: 2020},
    {imie: "Piotr", nazwisko: "Kowalczyk", rocznik: 2019},
    {imie: "Katarzyna", nazwisko: "Kowalska", rocznik: 2018}];


function StudentManager() {

    const [students, setStudents] = useState<Student[]>(Students);

    const addStudentFun = (student: Student) =>
        setStudents([...students, student])


    return (
        <>
            <table>
                <thead>
                <tr>
                    <th>Imię</th>
                    <th>Nazwisko</th>
                    <th>Rocznik</th>
                </tr>
                </thead>
                <tbody>
                {students.map((student, index) => (
                    <tr key={index}>
                        <td>{student.imie}</td>
                        <td>{student.nazwisko}</td>
                        <td>{student.rocznik}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            <br/>
            <Dodawanie addStudent={addStudentFun}/>
        </>
    );
}

export default StudentManager;