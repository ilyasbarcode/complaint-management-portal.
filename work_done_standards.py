"""Work Done remark strings observed in the supplied complaints.csv sample.

These are exact combined values (including capitalization, spacing and trailing commas),
not a guaranteed exhaustive list of every option in the technician application.
"""

WORK_DONE_STANDARD_VALUES = (
    'Condenser Service,',
    'Gas Charged,Condenser Service,',
    'Unit Wiring Repaired,',
    'Close Complaint,',
    'Relay Replaced,Capacitor Replaced,Condenser Service,',
    'FAN MOTOR 10W REPLACED,Condenser Service,',
    'Relay Replaced,Condenser Service,',
    'Only Checking,',
    'Compressor Replaced,Gas Charged,Condenser Service,',
    'Fan motor Oiling,',
    'FAN MOTOR 5W REPLACED,Condenser Service,',
    'Door Repaired,',
    'body rusted Not repairable,',
    'Close Complaint,Only Checking,',
    'Guide to Customer,',
    'Gas Kit Repaired,',
    'Compressor Replaced,Gas Charged,Relay Replaced,Condenser Service,',
    'Compressor Replaced,Gas Charged,Relay Replaced,Capacitor Replaced,Condenser Service,',
    'Not Repaireable,',
    'Gas Charged,',
    'Hinges Replaced Qnt 1,Condenser Service,',
    'Hinges Replaced Qnt 2,Condenser Service,',
    'OVERLOAD G326,VRS 19 & 540 EU Replaced,Condenser Service,',
    'Relay Adjusted,',
    'Compressor Replaced,Gas Charged,',
    'LED Replaced 1,Condenser Service,',
    'DOORREPAIRED,Condenser Service,',
    'Gas Charged,Relay Replaced,Capacitor Replaced,Condenser Service,',
    'Gas Charged,Relay Replaced,Condenser Service,',
    'Relay Replaced,FAN MOTOR 10W REPLACED,Capacitor Replaced,Condenser Service,',
    'Relay Replaced,FAN MOTOR 5W REPLACED,Condenser Service,',
    'Close Complaint,body rusted Not repairable,',
    'Compressor Replaced,Gas Charged,FAN MOTOR 10W REPLACED,Capacitor Replaced,OVERLOAD RELAY,Condenser Service,',
    'Compressor Replaced,Gas Charged,FAN MOTOR 5W REPLACED,Condenser Service,',
    'Compressor Replaced,Gas Charged,OVERLOAD RELAY,Condenser Service,',
    'Compressor Replaced,Gas Charged,Relay Replaced,Hinges Replaced Qnt 1,Capacitor Replaced,Condenser Service,',
    'DOOR GASKET CHEST-400SAX Replaced,Condenser Service,',
    'DOOR GASKET CHEST-400SAX Replaced,Hinges Replaced Qnt 2,Condenser Service,',
    'Gas Charged,Condenser Replaced,Condenser Service,',
    'Gas Charged,FAN MOTOR 10W REPLACED,Condenser Service,',
    'Gas Charged,Hinges Replaced Qnt 1,Condenser Service,',
    'OVERLOAD RELAY,Condenser Service,',
    'Relay Replaced,Capacitor Replaced,FAN MOTOR SD 16 W REPLACED,Condenser Service,',
    'Relay Replaced,FAN MOTOR 10W REPLACED,Condenser Service,',
    'Relay Replaced,Hinges Replaced Qnt 1,Capacitor Replaced,Condenser Service,',
    'Tube/LED Adjusted,',
    'Wheel Replaced Qnt 2,Condenser Service,',
)


def is_sample_standard_work_done(value):
    """Return True when value exactly matches a Work Done string in the sample."""
    return value in WORK_DONE_STANDARD_VALUES
