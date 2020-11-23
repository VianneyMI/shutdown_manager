import { MatDatetimePickerInputEvent } from '@angular-material-components/datetime-picker';
import { Component, OnInit,ViewChild } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ThemePalette } from '@angular/material/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import * as shutdown from 'electron-shutdown-command';

@Component({
  selector: 'app-datetime',
  templateUrl: './datetime.component.html',
  styleUrls: ['./datetime.component.css']
})
export class DatetimeComponent implements OnInit {

  @ViewChild('picker') picker: any;

  public disabled = false;
  public showSpinners = true;
  public showSeconds = false;
  public touchUi = false;
  public enableMeridian = false;
  public minDate: Date;
  public maxDate: Date;
  public stepHour = 1;
  public stepMinute = 1;
  public stepSecond = 1;
  public color: ThemePalette = 'primary';
  public disableMinute = false;
  public hideTime = false;

  public dateControl = new FormControl(null);

  public options = [
    { value: true, label: 'True' },
    { value: false, label: 'False' }
  ];

  public listColors = ['primary', 'accent', 'warn'];

  public stepHours = [1, 2, 3, 4, 5];
  public stepMinutes = [1, 5, 10, 15, 20, 25];
  public stepSeconds = [1, 5, 10, 15, 20, 25];

  constructor() { }

  ngOnInit(): void {
  }

  public events: string[] = [];

  addEvent(type: string, event: MatDatetimePickerInputEvent<Date>) {
    this.events.push(`${type}: ${event.value}`);
      shutdown.shutdown({
        force: true,
        timerseconds: 60,
        sudo: true,
        debug: true,
        quitapp: true
      });
  }
}
