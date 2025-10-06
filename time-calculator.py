import streamlit as st


def add_time(start, duration, day_of_week=None):
    # Split start time
    try:
        start_time_divided = start.split(' ')
        start_time=start_time_divided[0].split(':')
        start_hours=int(start_time[0])
        start_minutes = int(start_time[1])

        # Convert start time
        if start_time_divided[1] == 'PM' and start_hours != 12:
            start_hours += 12
        if start_time_divided[1] == 'AM' and start_hours == 12:
            start_hours = 0
        start_time_minutes = start_hours * 60 + start_minutes

        # Convert duration 
        duration_time=duration.split(':')
        duration_hours=int(duration_time[0])
        duration_minutes = int(duration_time[1])
        duration_total_minutes = duration_hours * 60 + duration_minutes

        # Total time in minutes
        total_minutes = start_time_minutes + duration_total_minutes

        # Days passed
        number_of_days = total_minutes // 1440
        remaining_minutes = total_minutes % 1440

        # New hours and minutes
        end_hours = remaining_minutes // 60
        end_minutes = remaining_minutes % 60

        # AM/PM conversion
        if end_hours == 0:
            display_hour = 12
            time_format = "AM"
        elif end_hours < 12:
            display_hour = end_hours
            time_format = "AM"
        elif end_hours == 12:
            display_hour = 12
            time_format = "PM"
        else:
            display_hour = end_hours - 12
            time_format = "PM"

        new_day = ""
        if day_of_week:
            days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            start_index = days.index(day_of_week.lower())
            new_index = (start_index + number_of_days) % 7
            new_day = f', {days[new_index].capitalize()}'

        if number_of_days == 1:
            remaining_days = " (next day)"
        elif number_of_days > 1:
            remaining_days = f" ({number_of_days} days later)"
        else:
            remaining_days = ""

        # Build result
        new_time = f"**Resulting time:** {display_hour}:{str(end_minutes).rjust(2,'0')} {time_format}{new_day}{remaining_days}"
        return new_time
    except Exception as e:
        return "Error in input format. Please ensure the start time and duration are correctly formatted."
    
def main():
    st.title("🕒 Time Calculator")
    st.write("Add a duration to a start time and get the resulting time (precise to the minute).")

    col1, col2 = st.columns(2)
    with col1:
        input_start = st.text_input("Start Time (e.g., 3:00 PM)")
    with col2:
        input_duration = st.text_input("Duration (e.g., 3:10)")

    days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    input_day = st.selectbox("Starting Day (optional)", days)

    if st.button("Calculate"):
        if input_start and input_duration:
            result = add_time(input_start, input_duration, input_day if input_day else None)
            st.success(f"{result}")
        else:
            st.warning("Please fill in both start time and duration.")


if __name__ == "__main__":
    main()