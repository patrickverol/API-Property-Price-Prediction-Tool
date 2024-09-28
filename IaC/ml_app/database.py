import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from contrato import EspecificacoesCasa, EspecificacoesCasaResponse

# Load environment variables
load_dotenv()

# PostgreSQL configuration
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Function to save the validated data to PostgreSQL
def salvar_no_postgres(dados: EspecificacoesCasa, host_name: str, estimated_price: EspecificacoesCasaResponse):
    """
    Function to save data to the PostgreSQL database
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Insert query to save data into especificacoes_casa table, including host_name and estimated_price
        insert_query = sql.SQL(
            """
            INSERT INTO especificacoes_casa (
                host_name, estimated_price, host_listings_count, latitude, longitude, accommodates, bathrooms, 
                bedrooms, beds, extra_people, minimum_nights, n_amenities, room_type_Entire_home_apt, host_is_superhost, 
                instant_bookable, ano, mes, property_type_Apartment, property_type_Bed_and_breakfast, property_type_Condominium, 
                property_type_Guest_suite, property_type_Guesthouse, property_type_Hostel, property_type_House, 
                property_type_Loft, property_type_Outros, property_type_Serviced_apartment, room_type_Hotel_room, 
                room_type_Private_room, room_type_Shared_room, cancellation_policy_flexible, cancellation_policy_moderate, 
                cancellation_policy_strict, cancellation_policy_strict_14_with_grace_period
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s)
            """
        )
        
        # Execute query with new values: host_name and estimated_price
        cursor.execute(insert_query, (
            host_name,
            estimated_price,
            dados.host_listings_count,
            dados.latitude,
            dados.longitude,
            dados.accommodates,
            dados.bathrooms,
            dados.bedrooms,
            dados.beds,
            dados.extra_people,
            dados.minimum_nights,
            dados.n_amenities,
            dados.room_type_Entire_home_apt,
            dados.host_is_superhost,
            dados.instant_bookable,
            dados.ano,
            dados.mes,
            dados.property_type_Apartment,
            dados.property_type_Bed_and_breakfast,
            dados.property_type_Condominium,
            dados.property_type_Guest_suite,
            dados.property_type_Guesthouse,
            dados.property_type_Hostel,
            dados.property_type_House,
            dados.property_type_Loft,
            dados.property_type_Outros,
            dados.property_type_Serviced_apartment,
            dados.room_type_Hotel_room,
            dados.room_type_Private_room,
            dados.room_type_Shared_room,
            dados.cancellation_policy_flexible,
            dados.cancellation_policy_moderate,
            dados.cancellation_policy_strict,
            dados.cancellation_policy_strict_14_with_grace_period
        ))
        
        conn.commit()
        cursor.close()
        conn.close()
        return "Dados salvos com sucesso no banco de dados!", 200
        
    except Exception as e:
        return f"Erro ao salvar no banco de dados: {e}", 500

