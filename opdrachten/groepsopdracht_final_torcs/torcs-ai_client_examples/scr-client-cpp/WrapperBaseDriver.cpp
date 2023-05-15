/***************************************************************************
 
    file                 : WrapperBaseDriver.cpp
    copyright            : (C) 2007 Daniele Loiacono
 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
#include "WrapperBaseDriver.h"

void writeCsvRow(CarState X, CarControl Y) {
	/**
     * CSV Representation
    */
    // X : Sensor Features from Server
    
    // 8 Car State Features
    //                                 s_speed_x;     s_speed_y;     s_speed_z;     s_rpm;      s_gear;       s_angle;      s_z;      s_damage;
    printf( "%f;%f;%f;%i;%i;%f;%f;%f", X.getSpeedX(), X.getSpeedY(), X.getSpeedZ(), X.getRpm(), X.getGear(),  X.getAngle(), X.getZ(), X.getDamage());
    //                                   -0.005887;     -0.027970;     0.000171;      942;        0;            0.000210;     0.345256; 0.000000

    // // 6 Race Environment Features
    // //                           s_track_position; s_race_position;s_distance_raced;s_distance_from_start;s_current_laptime; s_last_laptime 
    // printf( "%f;%i;%f;%f;%f;%f", X.getTrackPos(), X.getRacePos(), X.getDistRaced(), X.getDistFromStart(), X.getCurLapTime(), X.getLastLapTime());
    // //                           -0.333363;        1;              0.000000;         5759.100098;          -0.982000;         0.0000001.000000;

    // // Y : 5 Agent Actions
    // //                         a_accelation; a_brake;      a_gear;      a_steer;      a_clutch
    // printf("%f;%f;%i;%f;%f\n", Y.getAccel(), Y.getBrake(), Y.getGear(), Y.getSteer(), Y.getClutch());

}

string 
WrapperBaseDriver::drive(string sensors)
{
	CarState cs(sensors);
	CarControl cc = wDrive(cs);
    writeCsvRow(cs, cc);
	return cc.toString();	
}

